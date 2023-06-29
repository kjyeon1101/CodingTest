from itertools import combinations

def solution(nums):
    answer = 0
    for c in combinations(nums, 3):
        d = 2
        while sum(c) % d != 0:
            d += 1
        if d == sum(c):
            answer += 1
    return answer