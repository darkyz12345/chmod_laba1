from beautiful_tools.something import function, MethodResult, function_simple_iters, dif_function
from methods import bisection, simple_iteration, newton_raphson



if __name__ == "__main__":
    a = 0
    b = 1
    eps = 1e-10
    bisection_result: MethodResult = bisection(a, b, function, eps)
    simple_iteration_result: MethodResult = simple_iteration(0.7, eps, function_simple_iters)
    newton_raphson_result: MethodResult = newton_raphson(1, eps, function, dif_function)
    print(newton_raphson_result)
