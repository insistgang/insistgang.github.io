import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.t1_scorer import score_records


class T1ScorerTests(unittest.TestCase):
    def test_scores_valid_records_and_counts_invalid_as_zero(self):
        outputs = [
            {
                "student_id": "student_001",
                "raw_output": '{"student_id":"student_001","judgements":[true,false,true]}',
            },
            {
                "student_id": "student_002",
                "raw_output": '说明：{"student_id":"student_002","judgements":[true,true,true]}',
            },
        ]
        expected = {
            "student_001": [True, False, False],
            "student_002": [True, True, True],
        }
        result = score_records(outputs, expected)
        self.assertEqual(result.total_items, 6)
        self.assertEqual(result.correct_items, 2)
        self.assertEqual(result.invalid_records, 1)


if __name__ == "__main__":
    unittest.main()
