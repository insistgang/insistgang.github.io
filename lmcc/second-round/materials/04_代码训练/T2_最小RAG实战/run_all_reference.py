#!/usr/bin/env python3
"""Run all bundled T2 exercise reference outputs."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXERCISES = (
    "01_折扣检索入门",
    "02_单位换算检索",
    "03_应用题检索",
    "04_多步骤RAG",
    "05_近真题综合",
)


def main() -> int:
    for name in EXERCISES:
        print(f"\n=== {name} ===", flush=True)
        command = [
            sys.executable,
            str(ROOT / "batch_evaluate.py"),
            "--exercise",
            str(ROOT / "exercises" / name),
            "--answers",
            str(ROOT / "answers" / f"{name}_expected.jsonl"),
        ]
        if name == "01_折扣检索入门":
            command += ["--outputs", str(ROOT / "answers" / "01_demo_outputs.jsonl")]
        if subprocess.run(command, cwd=ROOT, check=False).returncode != 0:
            return 1
    print("\n✅ 5 道 T2 练习的检索与 JSON 样例全部通过。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
