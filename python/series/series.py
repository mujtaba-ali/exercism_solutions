def slices(series, length):
    if length <= 0 or length > len(series):
        raise ValueError("can't make substrings. provide a different length")
    sub_strings = []
    while len(series) >= length:
        sub_strings.append(series[:length])
        series = series[1:]
    return sub_strings
