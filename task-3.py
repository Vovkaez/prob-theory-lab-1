from scipy.stats import rv_discrete


def experimental_solution(p: float, max_value: int, num_tests: int, i: int, j: int):
    distribution = rv_discrete(values=(range(max_value), [(1 - p)**i * p for i in range(max_value)]))
    xs = distribution.rvs(size=num_tests)
    ys = distribution.rvs(size=num_tests)
    pairs = [(xs[k], ys[k]) for k in range(num_tests)]
    return sum(pair[0] == i and pair[1] == j - i for pair in pairs) / sum(pair[0] + pair[1] == j for pair in pairs)


def theoretical_solution(j: int):
    return 1 / (j + 1)


def compare_results(i: int, j: int, p: float, precision: float):
    return abs(theoretical_solution(j) - experimental_solution(p, 100000, 10000, i, j)) < precision


if __name__ == '__main__':
    p = 1/3
    i = 5
    j = 9
    assert(compare_results(i, j, p, 0.07))
    print('Tests passed')
