import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ExerciseAssetTests(unittest.TestCase):
    def test_five_exercises_keep_test_inputs_and_answers_separate(self):
        exercises = sorted(path for path in (ROOT / "exercises").iterdir() if path.is_dir())
        self.assertEqual(len(exercises), 5)
        for exercise in exercises:
            name = exercise.name
            bank_path = exercise / "data" / "problem_bank.json"
            data_path = exercise / "data" / "test_data.jsonl"
            answer_path = ROOT / "answers" / f"{name}_expected.jsonl"
            self.assertTrue(bank_path.is_file(), bank_path)
            self.assertTrue(data_path.is_file(), data_path)
            self.assertTrue(answer_path.is_file(), answer_path)
            inputs = [
                json.loads(line)
                for line in data_path.read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
            self.assertTrue(all({"id", "problem"} <= set(item) for item in inputs))
            self.assertNotIn('"answer"', data_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
