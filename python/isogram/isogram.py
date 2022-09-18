def is_isogram(string: str) -> bool:
    caseless = [c.casefold() for c in string if c.isalpha()]
    return len(caseless) == len(set(caseless))
