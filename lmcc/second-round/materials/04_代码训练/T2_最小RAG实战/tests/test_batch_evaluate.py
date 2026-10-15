import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.batch_evaluate import validate_raw_answer_output


class BatchEvaluateTests(unittest.TestCase):
    def test_accepts_strict_answer_json(self):
        result = validate_raw_answer_output(
            '{"reasoning":"120 × 0.8 = 96","answer":"96"}',
            expected_answer="96",
        )
        self.assertTrue(result.valid, result.errors)

    def test_rejects_extra_text_wrong_answer_and_non_numeric_answer(self):
        result = validate_raw_answer_output(
            '答案：{"reasoning":"ok","answer":"96元"}',
            expected_answer="96",
        )
        self.assertFalse(result.valid)
        self.assertIn("存在 JSON 外的多余文本", result.errors)

        result = validate_raw_answer_output(
            '{"reasoning":"ok","answer":"95"}',
            expected_answer="96",
        )
        self.assertFalse(result.valid)
        self.assertIn("answer 与期望答案不一致", result.errors)


if __name__ == "__main__":
    unittest.main()
