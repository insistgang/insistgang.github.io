"""Tiny Tensor shim for local T2 logic tests when PyTorch is unavailable.

It is intentionally limited to the operations used by the reference
submission: flatten, float, norm, matmul and item.  The official environment
must use real PyTorch tensors.
"""

from __future__ import annotations

import sys
import types


class TinyScalar:
    def __init__(self, value: float):
        self.value = float(value)

    def __mul__(self, other: "TinyScalar") -> "TinyScalar":
        return TinyScalar(self.value * other.value)

    def __truediv__(self, other: "TinyScalar") -> "TinyScalar":
        return TinyScalar(self.value / other.value)

    def item(self) -> float:
        return self.value


class TinyTensor:
    def __init__(self, values: list[float]):
        self.values = [float(value) for value in values]

    def flatten(self) -> "TinyTensor":
        return self

    def float(self) -> "TinyTensor":
        return self

    def norm(self) -> TinyScalar:
        return TinyScalar(sum(value * value for value in self.values) ** 0.5)

    def __matmul__(self, other: "TinyTensor") -> TinyScalar:
        return TinyScalar(sum(left * right for left, right in zip(self.values, other.values)))


def install_torch_shim() -> None:
    """Expose TinyTensor as a minimal torch module for local import tests."""
    sys.modules.setdefault("torch", types.SimpleNamespace(Tensor=TinyTensor))
