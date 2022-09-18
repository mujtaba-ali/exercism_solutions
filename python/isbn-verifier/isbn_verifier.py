def is_valid(isbn: str):
    if len(isbn) == 0 or len(isbn.replace("-","")) != 10:
        return False
    code = [int(c) for c in isbn if c.isnumeric()]
    if isbn[-1] == "X":
        code.append(10) 
    return sum([(10 - i)*j for i, j in enumerate(code)]) % 11 == 0
