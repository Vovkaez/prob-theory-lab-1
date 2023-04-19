from scipy.stats import rv_discrete
from math import sqrt, ceil, floor
from scipy.special import comb
from scipy.stats import norm
from math import exp, pi


def bernoulli_count_success(p: float, n: int) -> int:
    assert 0 <= p <= 1
    distribution = rv_discrete(values=([0, 1], [1 - p, p]))
    return sum(distribution.rvs(size=n))


def bernoulli_k_successes(p: float, n: int, k: int, num_tests: int) -> float:
    return sum(bernoulli_count_success(p, n) == k for _ in range(num_tests)) / num_tests


def approximate_solution(n: int, p: float) -> float:
    if p == 1/2:
        return norm.cdf(1) - norm.cdf(-1)

    q = 1 - p
    delta = sqrt(n * p * q)
    low = ceil(n / 2 - delta)
    high = floor(n / 2 + delta)

    return sum(exp(-(k - n * p)**2/(2 * n * p * q)) / sqrt(2 * pi * n * p * q)
               for k in range(low, high + 1))


def exact_solution(n: int, p: float) -> float:
    q = 1 - p
    delta = sqrt(n * p * q)
    low = ceil(n / 2 - delta)
    high = floor(n / 2 + delta)
    return sum(comb(n, k) * p ** k * q ** (n - k) for k in range(low, high + 1))


def experiment_solution(n: int, p: float, num_tests: int) -> float:
    q = 1 - p
    delta = sqrt(n * p * q)
    return sum(n / 2 - delta <= bernoulli_count_success(p, n) <= n / 2 + delta for _ in range(num_tests)) / num_tests


if __name__ == '__main__':
    ns = [10, 100, 1000, 10000]
    ps = [0.001, 0.01, 0.1, 0.25, 0.5]

    for n in ns:
        for p in ps:
            print(f'n = {n}, p = {p}')
            exact = exact_solution(n, p) if n != ns[-1] else experiment_solution(n, p, 1000)
            print(exact)
            print(approximate_solution(n, p))
