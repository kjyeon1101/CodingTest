import math

def solution(n):
    if math.pow(int(math.sqrt(n)), 2) == n:
        return math.pow(int(math.sqrt(n))+1, 2)
    else:
        return -1