import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from common.runner import mock_embedding


class RunnerTests(unittest.TestCase):
    def test_mock_embedding_is_deterministic_and_nonzero_for_text(self):
        first = mock_embedding("折扣 商品 原价")
        second = mock_embedding("折扣 商品 原价")
        self.assertEqual(first.values, second.values)
        self.assertGreater(first.norm().item(), 0)


if __name__ == "__main__":
    unittest.main()
