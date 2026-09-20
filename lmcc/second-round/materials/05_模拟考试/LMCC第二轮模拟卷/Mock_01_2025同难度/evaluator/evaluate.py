#!/usr/bin/env python3
import sys
from pathlib import Path

MOCK_DIR = Path(__file__).resolve().parents[1]
ROOT = MOCK_DIR.parent
sys.path.insert(0, str(ROOT))
from common.mock_runner import main_for_mock

if __name__ == "__main__":
    raise SystemExit(main_for_mock(MOCK_DIR))
