def primes(limit):
    numbers = list(range(2, limit + 1))
    for i, j in enumerate(numbers):
        for x in numbers[i+1:]:
            if x % j == 0: 
                numbers.remove(x)
    return numbers
