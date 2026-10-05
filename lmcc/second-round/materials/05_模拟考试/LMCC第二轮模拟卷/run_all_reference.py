#!/usr/bin/env python3
"""Run the bundled reference outputs against all three full mock exams."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MOCKS = ("Mock_01_2025同难度", "Mock_02_合理变式", "Mock_03_最终冲刺")


def main() -> int:
    for name in MOCKS:
        print(f"\n=== {name} ===", flush=True)
        mock_dir = ROOT / name
        command = [
            sys.executable,
            str(mock_dir / "evaluator" / "evaluate.py"),
            "--outputs",
            str(mock_dir / "answers" / "reference_outputs.jsonl"),
            "--scope",
            "full",
        ]
        if subprocess.run(command, cwd=ROOT, check=False).returncode != 0:
            return 1
    print("\n✅ 三套模拟卷的公开与隐藏集全部通过。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
