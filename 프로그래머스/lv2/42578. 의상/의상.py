from collections import Counter

def solution(clothes):
    answer = 1
    counter = Counter([c[1] for c in clothes])
    for c in counter:
        answer *= (counter[c] + 1)
    return answer - 1