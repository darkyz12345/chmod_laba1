from collections.abc import Callable

from beautiful_tools.something import MethodResult


def newton_raphson(
    x_0: float,
    eps: float,
    func: Callable[[float | int], float | int],
    dif_func: Callable[[float | int], float | int],
) -> MethodResult:
    """
    Newton-Raphson method for solving a nonlinear equation f(x) = 0.

    Args:
        x_0: Initial approximation.
        eps: Required accuracy.
        func: Function f(x).
        dif_func: Derivative f'(x).

    Returns:
        MethodResult: Result of the method.
    """
    fa: float = float(func(x_0))
    iterations: int = 0
    approximations: list[float] = []

    while abs(fa) > eps:
        fs: float = float(dif_func(x_0))

        if fs == 0:
            return MethodResult(
                root=x_0,
                iterations=iterations,
                error=abs(fa),
                approximations=approximations,
            )

        x_0 -= fa / fs

        iterations += 1
        approximations.append(x_0)

        fa = float(func(x_0))

    return MethodResult(
        root=x_0,
        iterations=iterations,
        error=abs(fa),
        approximations=approximations,
    )