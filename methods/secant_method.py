from collections.abc import Callable

from beautiful_tools.something import MethodResult


def secant(
    x_0: float | int,
    x_1: float | int,
    eps: float,
    func: Callable[[float | int], float | int],
) -> MethodResult:
    """
    Secant method for solving a nonlinear equation f(x) = 0.

    Args:
        x_0: First initial approximation.
        x_1: Second initial approximation.
        eps: Required accuracy.
        func: Function f(x).

    Returns:
        MethodResult: Result of the method.
    """
    iterations: int = 0
    approximations: list[float] = []
    while True:
        f0: float = float(func(x_0))
        f1: float = float(func(x_1))
        denominator = f1 - f0
        if denominator == 0:
            return MethodResult(
                root=x_1,
                iterations=iterations,
                error=abs(f1),
                approximations=approximations,
            )
        x: float = (x_0 * f1 - x_1 * f0) / denominator
        iterations += 1
        approximations.append(x)
        if abs(x - x_1) < eps:
            return MethodResult(
                root=x,
                iterations=iterations,
                error=abs(x - x_1),
                approximations=approximations,
            )
        x_0 = x_1
        x_1 = x