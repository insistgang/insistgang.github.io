import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOLUTION = ROOT / "standard_solution" / "submission.py"


def load_solution():
    spec = importlib.util.spec_from_file_location("t1_standard_submission", SOLUTION)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class T1SubmissionContractTests(unittest.TestCase):
    def test_prompt_covers_contract_and_official_answers(self):
        module = load_solution()
        prompt = module.build_system_prompt()
        for text in ("student_id", "judgements", "47", "22", "36", "325", "35"):
            self.assertIn(text, prompt)
        self.assertIn("只输出", prompt)
        self.assertIn("不要使用 Markdown", prompt)
        self.assertLess(len(prompt), 7000)

    def test_generation_parameters_are_deterministic_and_sufficient(self):
        module = load_solution()
        params = module.build_generation_parameters()
        self.assertFalse(params["do_sample"])
        self.assertTrue(params["enable_thinking"])
        self.assertGreaterEqual(params["max_new_tokens"], 512)


if __name__ == "__main__":
    unittest.main()
