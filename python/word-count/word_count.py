import string

def count_words(sentence):
    sentence = sentence.lower()
    spaces = ["\n", "\t", "_", ","]
    for i in spaces: sentence = sentence.replace(i, " ")
    translator = str.maketrans("", "", string.punctuation.replace("'", ""))
    sentence = sentence.translate(translator)
    words = {}

    for i in sentence.split():
        i = i.strip("'")
        if i in words.keys():
            words[i] += 1
        else:
            words[i] = 1

    return words
