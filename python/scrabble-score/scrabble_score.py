letters = "aeioulnsrtdgbcmpfhvwykjxqz"
scores = "111111111122333344444588XX"
mytable = str.maketrans(letters,scores)


def score(word):
    return sum([(10 if i == "X" else int(i)) for i in word.lower().translate(mytable)])
        
