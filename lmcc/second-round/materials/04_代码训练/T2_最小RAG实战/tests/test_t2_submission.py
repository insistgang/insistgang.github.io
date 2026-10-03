import importlib.util
import sys
import types
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOLUTION = ROOT / "standard_solution" / "submission.py"


class TinyScalar:
    def __init__(self, value):
        self.value = float(value)

    def __mul__(self, other):
        return TinyScalar(self.value * other.value)

    def __truediv__(self, other):
        return TinyScalar(self.value / other.value)

    def item(self):
        return self.value


class TinyTensor:
    def __init__(self, values):
        self.values = [float(value) for value in values]

    def flatten(self):
        return self

    def float(self):
        return self

    def norm(self):
        return TinyScalar(sum(value * value for value in self.values) ** 0.5)

    def __matmul__(self, other):
        return TinyScalar(sum(left * right for left, right in zip(self.values, other.values)))


def load_solution():
    sys.modules["torch"] = types.SimpleNamespace(Tensor=TinyTensor)
    spec = importlib.util.spec_from_file_location("t2_standard_submission", SOLUTION)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class T2SubmissionTests(unittest.TestCase):
    def test_cosine_similarity_handles_identity_opposite_and_zero_vector(self):
        module = load_solution()
        self.assertAlmostEqual(module.compute_similarity(TinyTensor([3, 4]), TinyTensor([3, 4])), 1.0)
        self.assertAlmostEqual(module.compute_similarity(TinyTensor([1, 0]), TinyTensor([-1, 0])), -1.0)
        self.assertEqual(module.compute_similarity(TinyTensor([0, 0]), TinyTensor([2, 1])), 0.0)

    def test_retrieval_returns_top_k_in_descending_similarity_order(self):
        module = load_solution()
        bank = [
            {"id": 1, "problem": "折扣商品", "answer": "60", "explanation": "原价乘折扣"},
            {"id": 2, "problem": "长方形面积", "answer": "24", "explanation": "长乘宽"},
            {"id": 3, "problem": "折扣会员", "answer": "80", "explanation": "计算八折"},
        ]
        vectors = {
            "查询折扣": TinyTensor([1, 0]),
            "折扣商品": TinyTensor([0.9, 0.1]),
            "长方形面积": TinyTensor([0, 1]),
            "折扣会员": TinyTensor([0.8, 0.2]),
        }
        retrieved = module.retrieve_relevant_problems(
            "查询折扣",
            bank,
            embedding_model=None,
            tokenizer=None,
            top_k=2,
            get_embedding_func=lambda text, _model, _tokenizer: vectors[text],
        )
        self.assertEqual([item["id"] for item in retrieved], [1, 3])

    def test_message_and_prompt_keep_current_problem_and_json_contract(self):
        module = load_solution()
        message = module.build_user_message(
            "当前问题：120 元打八折是多少？",
            [{"id": 1, "problem": "80 元打七五折", "answer": "60", "explanation": "80×0.75=60"}],
        )
        self.assertIn("当前问题", message)
        self.assertIn("参考题 1", message)
        self.assertIn("80 元打七五折", message)
        prompt = module.build_system_prompt()
        self.assertIn("reasoning", prompt)
        self.assertIn("answer", prompt)
        self.assertIn("只输出", prompt)
        self.assertFalse(module.build_generation_parameters()["do_sample"])


if __name__ == "__main__":
    unittest.main()
