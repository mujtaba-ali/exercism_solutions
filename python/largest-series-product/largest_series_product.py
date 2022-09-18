import math

def largest_product(series, size):

    if len(series) < size or any(c.isalpha() for c in series) or size < 0:
        raise ValueError("input the right size and make sure there are no alphabets")
    if size == 0:
        return 1

    prod = 0
    while len(series) >= size: prod = max(prod, math.prod([int(i) for i in series[:size]])); series = series[1:]

    return prod
