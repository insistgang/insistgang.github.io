#!/usr/bin/env python3
"""Run every reinforcement drill with the bundled reference outputs."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
QUESTION_NAMES = (
    "T1_01_答案提取",
    "T1_02_多数字干扰",
    "T1_03_单位与应用",
    "T1_04_近真题批改",
    "T2_01_折扣检索",
    "T2_02_单位检索",
    "T2_03_关系检索",
    "T2_04_近真题RAG",
    "综合_01_批改后检索",
    "综合_02_双任务限时",
)


def main() -> int:
    for name in QUESTION_NAMES:
        command = [
            sys.executable,
            str(ROOT / "questions" / name / "evaluate.py"),
            "--outputs",
            str(ROOT / "answers" / name / "demo_outputs.jsonl"),
            "--scope",
            "full",
        ]
        print(f"\n=== {name} ===", flush=True)
        completed = subprocess.run(command, cwd=ROOT, check=False)
        if completed.returncode != 0:
            return completed.returncode
    print("\n✅ 10 道强化题的公开与隐藏集全部通过。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
