def find_anagrams(word, candidates):
    return [i for i in candidates if sorted(i.casefold()) == sorted(word.casefold()) and i.casefold() != word.casefold()]
