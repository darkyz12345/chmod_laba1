from dataclasses import dataclass


def function(x: float|int) -> int|float:
    return x ** 3 + x - 1

@dataclass
class MethodResult:
    root: float
    iterations: int
    error: float
    approximations: list[float]