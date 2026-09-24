"""Chạy một mô hình ứng viên trên toàn bộ bộ thử (việc 2.2 + 2.4, spec P0-2).

Mỗi lượt gọi = (prompt, seed) -> một dòng JSON trong bench/raw/<key>__seed<k>.jsonl, ghi và
flush ngay. Chạy lại cùng lệnh sẽ BỎ QUA các lượt đã có -> Kaggle rớt phiên thì chạy tiếp được.
Seed đặt lại trước MỖI lượt nên kết quả không phụ thuộc thứ tự chạy hay việc chạy tiếp.

Không chấm điểm ở đây ngoài việc parse JSON để in tiến độ - chấm bằng bench/score.py trên
output thô, để sửa validator thì không phải chạy lại mô hình.

VRAM đo hai cách (spec P0-2 mục 3):
    vram_torch_peak_mb : torch.cuda.max_memory_allocated() của lượt gọi (reset trước mỗi lượt)
    vram_nvml_peak_mb  : đỉnh bộ nhớ đã dùng của cả card, lấy mẫu 20 lần/giây trong lượt gọi
                         (gồm CUDA context + phân mảnh - con số quyết định có vừa card hay không)

Chạy:
    python bench/run_infer.py --model qwen35-2b                      # đủ bộ thử x 3 seed
    python bench/run_infer.py --model qwen35-2b --seeds 0 --limit 2  # chạy thử
    python bench/run_infer.py --model qwen35-0.8b --quant none       # không lượng tử (máy thiếu bitsandbytes)
"""

from __future__ import annotations

import argparse
import gc
import json
import os
import platform
import subprocess
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from validator import extract_json  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MODELS = Path(__file__).parent / "models.yaml"
PROMPTS = Path("eval/prompts.jsonl")
SYSTEM_PROMPT = Path("bench/system_prompt.txt")


# ============================================================================ cấu hình

def load_spec(key: str) -> dict:
    doc = yaml.safe_load(MODELS.read_text(encoding="utf-8"))
    for m in doc["models"]:
        if m["key"] == key:
            spec = {**doc["defaults"], **m}
            spec["generation"] = {**doc["defaults"]["generation"], **m.get("generation", {})}
            spec["chat_kwargs"] = {**doc["defaults"]["chat_kwargs"], **m.get("chat_kwargs", {})}
            return spec
    sys.exit(f"Không có mô hình '{key}' trong {MODELS}. Có: {[m['key'] for m in doc['models']]}")


def load_prompts(args) -> list[dict]:
    recs = [json.loads(ln) for ln in PROMPTS.read_text(encoding="utf-8").splitlines() if ln.strip()]
    if args.families:
        recs = [r for r in recs if r["family"] in args.families]
    if args.ids:
        recs = [r for r in recs if r["id"] in args.ids]
    if args.limit:
        recs = recs[: args.limit]
    return recs


def done_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    out = set()
    for ln in path.read_text(encoding="utf-8").splitlines():
        try:
            rec = json.loads(ln)
        except json.JSONDecodeError:            # dòng cuối ghi dở khi phiên bị ngắt
            continue
        if not rec.get("error"):
            out.add(rec["prompt_id"])
    return out


# ============================================================================ đo VRAM cả card

class GpuMonitor:
    """Lấy mẫu bộ nhớ đã dùng của card vật lý đang chạy. Ưu tiên NVML, không có thì gọi nvidia-smi."""

    def __init__(self, torch_index: int = 0):
        visible = os.environ.get("CUDA_VISIBLE_DEVICES", "")
        ids = [x.strip() for x in visible.split(",") if x.strip()]
        self.index = int(ids[torch_index]) if ids and ids[torch_index].isdigit() else torch_index
        self.peak = 0.0
        self._stop = threading.Event()
        self._thread = None
        try:
            import pynvml
            pynvml.nvmlInit()
            handle = pynvml.nvmlDeviceGetHandleByIndex(self.index)
            self._read = lambda: pynvml.nvmlDeviceGetMemoryInfo(handle).used / 2**20
            self.backend, self.interval = "nvml", 0.05
        except Exception:
            self._read = self._smi
            self.backend, self.interval = "nvidia-smi", 0.5

    def _smi(self) -> float:
        out = subprocess.run(["nvidia-smi", "--query-gpu=memory.used", "--format=csv,noheader,nounits",
                              "-i", str(self.index)], capture_output=True, text=True, timeout=10)
        return float(out.stdout.strip().splitlines()[0])

    def now(self) -> float:
        try:
            return self._read()
        except Exception:
            return float("nan")

    def _loop(self) -> None:
        while not self._stop.is_set():
            v = self.now()
            if v == v:
                self.peak = max(self.peak, v)
            self._stop.wait(self.interval)

    def start(self) -> None:
        self.peak = self.now()
        self._stop.clear()
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def stop(self) -> float:
        self._stop.set()
        if self._thread:
            self._thread.join()
        return round(self.peak, 1)


# ============================================================================ nạp mô hình

def move_to_cpu(model, dotted: str) -> str:
    """Bảng embedding -> giữ ở CPU nhưng trả output về GPU (tra cứu rẻ, tiết kiệm VRAM);
    module khác (tháp ảnh/âm thanh, không dùng khi chỉ có văn bản) -> chuyển thẳng sang CPU."""
    import torch
    from torch import nn

    class OnCPU(nn.Module):
        def __init__(self, inner):
            super().__init__()
            self.inner = inner.to("cpu")

        def forward(self, x, *a, **k):
            return self.inner(x.to("cpu"), *a, **k).to(x.device)

    parent_path, _, attr = dotted.rpartition(".")
    parent = model.get_submodule(parent_path) if parent_path else model
    module = getattr(parent, attr, None)
    if module is None:
        return f"{dotted}: không có"
    if isinstance(module, nn.Embedding):
        setattr(parent, attr, OnCPU(module))
        return f"{dotted}: embedding -> CPU (bọc)"
    module.to("cpu")
    torch.cuda.empty_cache()
    return f"{dotted}: -> CPU"


def load_model(spec: dict, quant: str, local_path: str | None = None):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

    dtype = getattr(torch, spec["compute_dtype"])
    source = local_path or spec["id"]
    rev = {} if local_path else {"revision": spec["revision"]}
    tok = AutoTokenizer.from_pretrained(source, **rev)
    kwargs = {**rev, "dtype": dtype}
    if quant == "nf4":
        skip = spec.get("skip_quant_modules")
        kwargs["quantization_config"] = BitsAndBytesConfig(
            load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=dtype,
            llm_int8_skip_modules=(skip + ["lm_head"]) if skip else None,
        )
        kwargs["device_map"] = {"": 0}

    t0 = time.time()
    model = AutoModelForCausalLM.from_pretrained(source, **kwargs)
    if quant == "none":
        model.to("cuda")
    model.eval()
    placement = [move_to_cpu(model, m) for m in spec.get("cpu_modules", [])]
    gc.collect()
    torch.cuda.empty_cache()
    return tok, model, round(time.time() - t0, 1), placement


def build_prompt(tok, system: str, user: str, chat_kwargs: dict) -> tuple[str, str]:
    msgs = [{"role": "system", "content": system}, {"role": "user", "content": user}]
    try:
        return tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True, **chat_kwargs), "system"
    except Exception:                             # mẫu chat không nhận vai system -> gộp vào user
        msgs = [{"role": "user", "content": system + "\n\n" + user}]
        return tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True, **chat_kwargs), "merged"


def param_counts(model) -> dict:
    import torch
    on_gpu = sum(p.numel() for p in model.parameters() if p.device.type == "cuda")
    total = sum(p.numel() for p in model.parameters())
    # tham số 4-bit bị đóng gói 2 giá trị/byte -> numel() đếm thiếu một nửa; chỉ dùng để tham khảo
    return {"numel_total": total, "numel_on_gpu": on_gpu,
            "cuda_allocated_mb": round(torch.cuda.memory_allocated() / 2**20, 1)}


# ============================================================================ chạy

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, help="key trong bench/models.yaml")
    ap.add_argument("--seeds", type=int, nargs="*", help="mặc định lấy từ models.yaml")
    ap.add_argument("--limit", type=int, help="chỉ chạy N prompt đầu (chạy thử)")
    ap.add_argument("--families", nargs="*", help="lọc họ, ví dụ F1 F2")
    ap.add_argument("--ids", nargs="*", help="lọc prompt id")
    ap.add_argument("--quant", choices=["nf4", "none"], help="mặc định lấy từ models.yaml")
    ap.add_argument("--out", default="bench/raw")
    ap.add_argument("--local-path", help="nạp từ thư mục đã tải sẵn (đúng revision trong models.yaml)")
    args = ap.parse_args()

    import torch
    import transformers
    from transformers import GenerationConfig, set_seed

    if not torch.cuda.is_available():
        sys.exit("Không thấy GPU CUDA.")
    spec = load_spec(args.model)
    quant = args.quant or spec["quant"]
    seeds = args.seeds if args.seeds is not None else spec["seeds"]
    prompts = load_prompts(args)
    system = SYSTEM_PROMPT.read_text(encoding="utf-8")
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    tag = args.model if quant == spec["quant"] else f"{args.model}+{quant}"

    todo = {s: [p for p in prompts if p["id"] not in done_ids(out_dir / f"{tag}__seed{s}.jsonl")] for s in seeds}
    n_todo = sum(len(v) for v in todo.values())
    print(f"[{tag}] {spec['id']}@{spec['revision'][:8]} | {len(prompts)} prompt x seed {seeds} | còn {n_todo} lượt")
    if n_todo == 0:
        return

    monitor = GpuMonitor()
    idle_mb = monitor.now()
    tok, model, load_s, placement = load_model(spec, quant, args.local_path)
    load_mb = monitor.now()
    print(f"  nạp xong {load_s}s | VRAM card: trước {idle_mb:.0f} MB -> sau nạp {load_mb:.0f} MB "
          f"| torch {torch.cuda.memory_allocated() / 2**20:.0f} MB | đo bằng {monitor.backend}")
    for p in placement:
        print("  ", p)

    gen = GenerationConfig.from_dict({**model.generation_config.to_dict(), **spec["generation"]})
    # Dừng ở CẢ eos của mô hình lẫn eos của mẫu chat: Qwen3.5 khai eos = <|endoftext|> nhưng
    # lượt trả lời kết thúc bằng <|im_end|> - thiếu cái sau thì sinh tràn, sai số đo tốc độ.
    eos = gen.eos_token_id if isinstance(gen.eos_token_id, list) else [gen.eos_token_id]
    gen.eos_token_id = sorted({e for e in eos + [tok.eos_token_id] if e is not None})
    if gen.pad_token_id is None:
        gen.pad_token_id = tok.pad_token_id if tok.pad_token_id is not None else tok.eos_token_id
    max_ctx = spec.get("max_context")

    # làm nóng: lượt đầu tiên chậm bất thường (biên dịch kernel, cấp phát cache) -> không tính
    warm, _ = build_prompt(tok, system, prompts[0]["instruction"], spec["chat_kwargs"])
    with torch.no_grad():
        model.generate(**tok(warm, return_tensors="pt", add_special_tokens=False).to("cuda"),
                       generation_config=GenerationConfig.from_dict({**gen.to_dict(), "max_new_tokens": 8}))

    meta = {
        "key": tag, "model_id": spec["id"], "revision": spec["revision"], "quant": quant,
        "compute_dtype": spec["compute_dtype"], "generation": spec["generation"],
        "chat_kwargs": spec["chat_kwargs"], "cpu_modules": placement,
        "load_s": load_s, "vram_idle_mb": idle_mb, "vram_after_load_mb": load_mb,
        **param_counts(model),
        "gpu": torch.cuda.get_device_name(0), "vram_backend": monitor.backend,
        "versions": {"python": platform.python_version(), "torch": torch.__version__,
                     "cuda": torch.version.cuda, "transformers": transformers.__version__,
                     "bitsandbytes": _version("bitsandbytes")},
        "started": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    (out_dir / f"{tag}__meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")

    n_done, n_json, t_start = 0, 0, time.time()
    for seed in seeds:
        path = out_dir / f"{tag}__seed{seed}.jsonl"
        with path.open("a", encoding="utf-8") as fh:
            for p in todo[seed]:
                text, sys_mode = build_prompt(tok, system, p["instruction"], spec["chat_kwargs"])
                enc = tok(text, return_tensors="pt", add_special_tokens=False).to("cuda")
                n_in = enc["input_ids"].shape[1]
                rec = {"prompt_id": p["id"], "family": p["family"], "pair_id": p["pair_id"],
                       "model": tag, "model_id": spec["id"], "revision": spec["revision"], "seed": seed,
                       "system_mode": sys_mode, "n_prompt_tokens": n_in}

                if max_ctx and n_in + gen.max_new_tokens > max_ctx:
                    rec.update(error="context_overflow", raw_output="", formulas=None, json_ok=False)
                else:
                    set_seed(seed)
                    torch.cuda.reset_peak_memory_stats()
                    monitor.start()
                    torch.cuda.synchronize()
                    t0 = time.perf_counter()
                    try:
                        with torch.no_grad():
                            out = model.generate(**enc, generation_config=gen)
                        torch.cuda.synchronize()
                        latency = time.perf_counter() - t0
                        new = out[0, n_in:]
                        raw = tok.decode(new, skip_special_tokens=True)
                        formulas, err = extract_json(raw)
                        rec.update(
                            raw_output=raw, formulas=formulas, json_ok=formulas is not None, json_error=err,
                            n_gen_tokens=int(new.shape[0]),
                            hit_max_tokens=int(new.shape[0]) >= gen.max_new_tokens,
                            latency_s=round(latency, 3),
                            tok_per_s=round(int(new.shape[0]) / latency, 2) if latency > 0 else None,
                            vram_torch_peak_mb=round(torch.cuda.max_memory_allocated() / 2**20, 1),
                            vram_nvml_peak_mb=monitor.stop(),
                        )
                    except torch.cuda.OutOfMemoryError:
                        monitor.stop()
                        torch.cuda.empty_cache()
                        rec.update(error="oom", raw_output="", formulas=None, json_ok=False)

                rec["timestamp"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
                fh.flush()

                n_done += 1
                n_json += bool(rec.get("json_ok"))
                if n_done % 10 == 0 or n_done == n_todo or rec.get("error"):
                    el = time.time() - t_start
                    eta = el / n_done * (n_todo - n_done)
                    print(f"  seed {seed} {p['id']:7s} {n_done}/{n_todo} | JSON ok {n_json / n_done:.0%} "
                          f"| {rec.get('latency_s', '-')}s {rec.get('tok_per_s', '-')} tok/s "
                          f"| VRAM {rec.get('vram_nvml_peak_mb', '-')} MB | còn ~{eta / 60:.0f} phút"
                          + (f" | LỖI {rec['error']}" if rec.get("error") else ""), flush=True)

    print(f"[{tag}] xong {n_done} lượt trong {(time.time() - t_start) / 60:.1f} phút -> {out_dir}")


def _version(pkg: str) -> str | None:
    try:
        from importlib.metadata import version
        return version(pkg)
    except Exception:
        return None


if __name__ == "__main__":
    main()
