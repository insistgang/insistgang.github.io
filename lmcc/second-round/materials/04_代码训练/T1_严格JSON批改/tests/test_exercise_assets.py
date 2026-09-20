import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXERCISES = ROOT / "exercises"
ANSWERS = ROOT / "answers"


class ExerciseAssetTests(unittest.TestCase):
    def test_five_exercises_have_isolated_data_and_hidden_answers(self):
        exercise_dirs = sorted(path for path in EXERCISES.iterdir() if path.is_dir())
        self.assertEqual(len(exercise_dirs), 5)
        for exercise_dir in exercise_dirs:
            data_path = exercise_dir / "data" / "test_data.jsonl"
            prompt_path = exercise_dir / "题目.md"
            answer_path = ANSWERS / f"{exercise_dir.name}_expected.jsonl"
            self.assertTrue(data_path.is_file(), data_path)
            self.assertTrue(prompt_path.is_file(), prompt_path)
            self.assertTrue(answer_path.is_file(), answer_path)
            self.assertNotIn("expected_judgements", prompt_path.read_text(encoding="utf-8"))
            records = [
                json.loads(line)
                for line in data_path.read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
            self.assertGreaterEqual(len(records), 2)
            self.assertTrue(all({"student_id", "content"} <= set(record) for record in records))


if __name__ == "__main__":
    unittest.main()
