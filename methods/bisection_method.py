from collections.abc import Callable
from beautiful_tools.something import MethodResult


def bisection(a: int|float, 
                     b: int|float, 
                    func: Callable[[int|float], int|float],
                    eps: float) -> MethodResult:
    """

    Args:
        a (int | float): start of segment
        b (int | float): end of segment
        func (callable[[int | float], int | float]): function of equation f(x)=0
        eps (float): accuracy

    Returns:
        MethodResult: result of method 
    """
    fa, fb = func(a), func(b)
    if fa == 0:
        return 0, a, .0
    if fb == 0:
        return 0, b, .0
    if fa * fb >= 0:
        raise ValueError("Функция должна иметь разные знаки на концах отрезка [a, b]")
    iterations: int = 0
    approximations: list[float] = []
    while (b - a) / 2 > eps:
        midpoint: float = (a + b) / 2
        fm: float = func(midpoint)
        iterations += 1
        approximations.append(midpoint)
        if abs(fm) < eps:
            return MethodResult(root=midpoint,
                                iterations=iterations,
                                error=(b - a) / 2,
                                approximations=approximations)
        if fa * fm < 0:
            b = midpoint
        else:
            a = midpoint
            fa = fm
    return MethodResult(root=midpoint,
                        iterations=iterations,
                        error=(b - a) / 2,
                        approximations=approximations)