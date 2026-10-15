import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from common.contracts import validate_t1_output, validate_t2_output


class ContractTests(unittest.TestCase):
    def test_t1_requires_pure_json_boolean_array_and_matching_id(self):
        result = validate_t1_output(
            '{"student_id":"s1","judgements":[true,false,true]}',
            student_id="s1",
            expected_count=3,
        )
        self.assertTrue(result.valid, result.errors)

        result = validate_t1_output(
            '结果：{"student_id":"s1","judgements":[true,0,true]}',
            student_id="s1",
            expected_count=3,
        )
        self.assertFalse(result.valid)
        self.assertIn("存在 JSON 外的多余文本", result.errors)

    def test_t2_requires_pure_json_and_numeric_string_answer(self):
        result = validate_t2_output(
            '{"reasoning":"120 × 0.8 = 96","answer":"96"}',
            expected_answer="96",
        )
        self.assertTrue(result.valid, result.errors)

        result = validate_t2_output(
            '{"reasoning":"ok","answer":"96元"}',
            expected_answer="96",
        )
        self.assertFalse(result.valid)
        self.assertIn("answer 必须只包含数字", result.errors)


if __name__ == "__main__":
    unittest.main()
