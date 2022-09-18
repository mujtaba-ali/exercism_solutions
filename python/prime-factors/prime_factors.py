def factors(value):
    primes = []
    i = 2

    while i * i <= value:
        if value % i == 0:
            value //= i
            primes.append(i)
        else:
            i += 1

    if value > 1:
        primes.append(value)

    return primes
