from itertools import combinations

def solution(numbers):
    answer = []
    for c in combinations(numbers, 2):
        answer.append(c[0] + c[1])
    return sorted(list(set(answer)))