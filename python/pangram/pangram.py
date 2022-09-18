def is_pangram(sentence: str):
    alphabets = [c.lower() for c in sentence if c.isalpha()]
    return len(set(alphabets)) == 26
