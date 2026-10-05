import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class MockAssetTests(unittest.TestCase):
    def test_three_complete_mock_directories_exist(self):
        mocks = sorted(path for path in ROOT.iterdir() if path.name.startswith("Mock_"))
        self.assertEqual(len(mocks), 3)
        for mock in mocks:
            for required in ("exam", "data", "evaluator", "answers"):
                self.assertTrue((mock / required).is_dir(), f"{mock.name}/{required}")
            self.assertTrue((mock / "README.md").is_file())
            self.assertTrue((mock / "exam" / "T1" / "submission.py").is_file())
            self.assertTrue((mock / "exam" / "T2" / "submission.py").is_file())
            self.assertTrue((mock / "evaluator" / "evaluate.py").is_file())
            self.assertTrue((mock / "answers" / "标准答案.md").is_file())
            self.assertTrue((mock / "answers" / "解析.md").is_file())
