#!/usr/bin/env python3
"""Per-question entrypoint.  Shared grading logic stays in common/runner.py."""

import sys
from pathlib import Path


QUESTION_DIR = Path(__file__).resolve().parent
TRAINING_ROOT = QUESTION_DIR.parents[1]
sys.path.insert(0, str(TRAINING_ROOT))

from common.runner import main_for_question


if __name__ == "__main__":
    raise SystemExit(main_for_question(QUESTION_DIR))
