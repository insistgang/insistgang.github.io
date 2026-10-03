import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from common.contracts import validate_t1_output, validate_t2_output


class MockContractTests(unittest.TestCase):
    def test_t1_requires_exact_json_boolean_contract(self):
        ok = validate_t1_output(
            '{"student_id":"s1","judgements":[true,false,true]}',
            student_id="s1",
            expected_count=3,
        )
        self.assertTrue(ok.valid, ok.errors)
        bad = validate_t1_output(
            '结果：{"student_id":"s1","judgements":[true,false,true]}',
            student_id="s1",
            expected_count=3,
        )
        self.assertFalse(bad.valid)

    def test_t2_requires_exact_json_numeric_answer(self):
        ok = validate_t2_output('{"reasoning":"2 × 3 = 6","answer":"6"}', expected_answer="6")
        self.assertTrue(ok.valid, ok.errors)
        bad = validate_t2_output('{"reasoning":"ok","answer":"6元"}', expected_answer="6")
        self.assertFalse(bad.valid)
