number_dict = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
               7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
               13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
               17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
               30: "thirty", 40: "fourty", 50: "fifty", 60: "sixty", 70: "seventy",
               80: "eighty", 90: "ninety"}
bigger = ["trillion", "billion", "million", "thousand"]


def say(number):
    num_str = str(number)
    num_split = []

    initial = ""
    while len(num_str) % 3 != 0:
        initial += num_str[0]
        num_str = num_str[1:]
    if initial != "":
        num_split.append(word(initial))

    while len(num_str) > 0:
        num_split.append(word(num_str[:3]))
        num_str = num_str[3:]

    i = len(num_split) - 1
    while i > 0:
        num_split.insert(i, f" {bigger[-1]} ")
        del bigger[-1]
        i -= 1
    return "".join(num_split)


def word(num_str):
    num_words = []
    huns_tens = []
    word_str = ""

    if len(num_str) > 2:
        huns_tens.append(num_str[0])
        huns_tens.append(num_str[1:3])

    else:
        huns_tens.append(0)
        huns_tens.append(num_str[:])

    if int(huns_tens[1]) in range(11, 20):
        num_words.append(number_dict[int(huns_tens[1])])
    else:
        for i,j in enumerate(huns_tens[1][::-1]):
            num_words.append(number_dict[int(j)*(10**i)])

    if huns_tens[0] != 0:
        word_str += number_dict[int(huns_tens[0])]+" hundred "

    if "0" not in huns_tens[1]:
        word_str += ("-".join(num_words[::-1]))
    else:
        word_str += "".join(num_words[::-1])

    return word_str
