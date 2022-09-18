def classify(number):
    if number < 1:
        raise ValueError("provide a number higher than 0")

    total = factors_total(number)

    if total > number: return "abundant"
    elif total < number: return "deficient"
    else: return "perfect"


def factors_total(number):
    if number == 1: return 0

    factors = [1]
    i = 2

    while i * i <= number:
        if number % i == 0:
            factors.append(i)
            if number//i != i: factors.append(number//i)
        i += 1

    return sum(factors)
