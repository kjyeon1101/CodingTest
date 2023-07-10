from itertools import product

def solution(word):
    alphabet = ["A", "E", "I", "O", "U"]
    dictionary = []
    for i in range(1, 6):
        for a in product(alphabet, repeat=i):
            dictionary.append("".join(a))
            if "".join(a) == word:
                break
    dictionary = sorted(dictionary)
    answer = dictionary.index(word)+1
    return answer