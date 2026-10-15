import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.t1_validator import validate_raw_output


class T1ValidatorTests(unittest.TestCase):
    def test_accepts_exact_contract_json(self):
        result = validate_raw_output(
            '{"student_id":"student_001","judgements":[true,false,true]}',
            expected_student_id="student_001",
            expected_count=3,
        )
        self.assertTrue(result.valid, result.errors)

    def test_rejects_extra_text_even_when_json_can_be_extracted(self):
        result = validate_raw_output(
            '结果如下：{"student_id":"student_001","judgements":[true,false,true]}',
            expected_student_id="student_001",
            expected_count=3,
        )
        self.assertFalse(result.valid)
        self.assertIn("存在 JSON 外的多余文本", result.errors)

    def test_rejects_missing_or_wrong_typed_fields(self):
        result = validate_raw_output(
            '{"student_id":"student_001","judgements":[1,false,true]}',
            expected_student_id="student_001",
            expected_count=3,
        )
        self.assertFalse(result.valid)
        self.assertIn("judgements[0] 必须是 JSON 布尔值", result.errors)

    def test_rejects_wrong_id_and_length(self):
        result = validate_raw_output(
            '{"student_id":"student_999","judgements":[true,false]}',
            expected_student_id="student_001",
            expected_count=3,
        )
        self.assertFalse(result.valid)
        self.assertIn("student_id 与输入不一致", result.errors)
        self.assertIn("judgements 长度应为 3，实际为 2", result.errors)


if __name__ == "__main__":
    unittest.main()
