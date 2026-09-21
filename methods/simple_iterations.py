from beautiful_tools.something import MethodResult
from collections.abc import Callable


def simple_iteration(
    x_0: float | int,
    eps: float,
    func: Callable[[float | int], float | int],
) -> MethodResult:
    """Simple iteration method.

    Args:
        x_0: Initial approximation.
        eps: Required accuracy.
        func: Iteration function φ(x).

    Returns:
        MethodResult: Result of the method.
    """
    iterations: int = 0
    approximations: list[float] = []

    while True:
        x = float(func(x_0))
        approximations.append(x)
        iterations += 1

        delta = abs(x - x_0)

        if delta < eps:
            break

        x_0 = x

    return MethodResult(
        root=x,
        iterations=iterations,
        error=delta,
        approximations=approximations,
    )