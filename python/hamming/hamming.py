def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("Both Strands should be equal")
    return sum(1 for i, j in zip(strand_a, strand_b) if i != j)

