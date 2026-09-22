import matplotlib.pyplot as plt
import numpy as np 

from methods import (bisection, 
                    simple_iteration,
                    newton_raphson,
                    secant)

from beautiful_tools.something import (function,
                                       MethodResult,
                                       function_simple_iters,
                                       dif_function)



if __name__ == "__main__":
    a = 0
    b = 1
    eps = 1e-10
    results = {
        'Метод бисекции': bisection(a, b, function, eps),
        'Метод простых итераций': simple_iteration(0.7, eps, function_simple_iters),
        'Метод Ньютона-Рафсона': newton_raphson(b, eps, function, dif_function),
        'Метод секущих': secant(a, b, eps, function)
    }
    #first graph
    x = np.linspace(-1 * b, b, 1500)
    y = function(x)
    root = results['Метод Ньютона-Рафсона'].root
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=r"$f(x)=x^3+x-1$")
    plt.axhline(0, linewidth=0.8)
    plt.scatter(root,
                function(root),
                label=fr"$x^* \approx{root:.10f}$",
                zorder=3,)
    plt.xlabel("$x$")
    plt.ylabel("$f(x)$")
    plt.title("График функции и найденное решение")
    plt.grid()
    plt.legend()
    plt.savefig("images/graph_sol.png")

    #second graph
    plt.figure(figsize=(8, 5))
    for name, result in results.items():
        iterations = np.arange(1, len(result.approximations) + 1)
        plt.plot(
            iterations,
            result.approximations,
            marker="o",
            label=name,
        )
    plt.xlabel("Номер итерации $n$")
    plt.ylabel("$x_n$")
    plt.title("Зависимость приближений $x_n$ от номера итерации")
    plt.grid()
    plt.legend()
    plt.savefig("images/graph_x_n.png")

    #third graph
    reference_root = newton_raphson(
        b,
        1e-15,
        function,
        dif_function
    ).root
    plt.figure(figsize=(8, 5))
    for name, result in results.items():
        errors = np.array([
            abs(x_n - reference_root)
            for x_n in result.approximations
        ])
        iterations = np.arange(1, len(errors) + 1,)
        plt.semilogy(
            iterations,
            errors,
            marker="o",
            label=name,
        )
    plt.xlabel("Номер итерации $n$")
    plt.ylabel(r"$|x_n-x^*$")
    plt.title("Погрешность приближений")
    plt.grid()
    plt.legend()
    plt.savefig("images/graph_x_n_x.png")

    #table
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.axis("off")
    table_data = []
    for name, result in results.items():
        table_data.append([
            name, f"{result.root:.10f}",
            result.iterations,
            f"{result.error:.3e}",
        ])
    table = ax.table(
        cellText=table_data,
        colLabels=[
            "Название метода",
            "Найденное решение",
            "Количество итераций",
            "Погрешность"
        ],
        loc="center",
        cellLoc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    plt.title("Результаты вычислений")
    plt.savefig("images/table.png")
    plt.show()