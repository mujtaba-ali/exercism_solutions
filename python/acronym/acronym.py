def abbreviate(words):
    for i in ["-", "_"]: words = words.replace(i, " ") 
    return "".join([i[0].upper() for i in words.split()])
