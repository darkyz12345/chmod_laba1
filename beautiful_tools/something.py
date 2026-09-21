from dataclasses import dataclass


def function(x: float|int) -> int|float:
    return x ** 3 + x - 1

def function_simple_iters(x: float|int) -> float|int:
    return (1 - x) ** (1/3)

@dataclass
class MethodResult:
    root: float
    iterations: int
    error: float
    approximations: list[float]