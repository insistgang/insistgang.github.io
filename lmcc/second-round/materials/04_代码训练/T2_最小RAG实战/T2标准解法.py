"""快捷入口：T2 的标准解法在 standard_solution/submission.py。"""

from standard_solution.submission import (
    build_generation_parameters,
    build_system_prompt,
    build_user_message,
    compute_similarity,
    retrieve_relevant_problems,
)


__all__ = [
    "compute_similarity",
    "retrieve_relevant_problems",
    "build_user_message",
    "build_system_prompt",
    "build_generation_parameters",
]
