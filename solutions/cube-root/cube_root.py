def improve(n, guess):
    return (n / guess**2 + 2 * guess) / 3


def cub_root(n):
    accuracy = 0.01
    result = improve(n, 1)
    while abs(n - result**3) > accuracy:
        result = improve(n, result)
    return result
