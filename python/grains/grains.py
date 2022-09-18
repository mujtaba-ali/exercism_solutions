def square(number: int) -> int:
    if number < 1 or number > 64:
        raise ValueError("input the correct board square")
    return 2**(number - 1)    


def total() -> int:
    return sum([square(i) for i in range(1, 65)])
