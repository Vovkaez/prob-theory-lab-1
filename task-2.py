from math import sqrt, log
import scipy.integrate as integrate


def parabola_length(r: float) -> float:
    return integrate.quad(lambda x: sqrt(1 + 4*(x ** 2)), 0, r)[0]


def simulation_solution() -> float:
    return parabola_length(sqrt(3) / 2) / parabola_length(2)


def theoretical_solution() -> float:
    def integral(x: float) -> float:
        return 1/2 * x * sqrt(1 + 4 * x**2) + 1/4 * log(2 * x + sqrt(1 + 4 * x**2))

    return integral(sqrt(3) / 2) / integral(2)


def compare_results(precision: float) -> bool:
    return abs(simulation_solution() - theoretical_solution()) < precision


if __name__ == '__main__':
    print(theoretical_solution())
    assert compare_results(1e-9)
    print('Tests passed')
