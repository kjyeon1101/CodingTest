from itertools import permutations

def solution(numbers):
    answer = 0
    p_set = set()
    
    for i in range(1, len(numbers)+1):
        for p in permutations(list(numbers), i):
            n = int("".join(p))
            if n != 0 and n!= 1:
                p_set.add(n)
            
    for p in p_set:
        d = 2
        while p % d != 0:
            d += 1
        if p == d:
            answer += 1
    
    return answer