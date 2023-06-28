from itertools import combinations

def solution(number):
    answer = [sum(i) for i in combinations(number, 3)].count(0)
    return answer