from beautiful_tools.something import function
from methods.bisection_method import bisection_method


if __name__ == "__main__":
    a = 0
    b = 1
    eps = 1e-10
    print(bisection_method(a, b, function, eps))
