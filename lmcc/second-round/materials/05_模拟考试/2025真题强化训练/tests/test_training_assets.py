import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TrainingAssetTests(unittest.TestCase):
    def test_exactly_ten_question_directories_exist(self):
        question_dirs = sorted(path for path in (ROOT / "questions").iterdir() if path.is_dir())
        self.assertEqual(len(question_dirs), 10)
        names = [path.name for path in question_dirs]
        self.assertEqual(sum(name.startswith("T1_") for name in names), 4)
        self.assertEqual(sum(name.startswith("T2_") for name in names), 4)
        self.assertEqual(sum(name.startswith("综合_") for name in names), 2)
        for directory in question_dirs:
            self.assertTrue((directory / "题目.md").is_file())
            self.assertTrue((directory / "starter.py").is_file())
            self.assertTrue((directory / "evaluate.py").is_file())
            self.assertTrue((directory / "spec.json").is_file())
            self.assertTrue((directory / "data").is_dir())
            answer_dir = ROOT / "answers" / directory.name
            self.assertTrue(answer_dir.is_dir())
            self.assertTrue(any(answer_dir.glob("*_hidden_data.jsonl")))
            self.assertTrue(any(answer_dir.glob("*_hidden_expected.jsonl")))


if __name__ == "__main__":
    unittest.main()
