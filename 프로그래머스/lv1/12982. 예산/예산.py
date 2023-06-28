def solution(d, budget):
    answer = 0
    for b in sorted(d):
        budget -= b
        answer += 1
        if budget < 0:
            return answer - 1
    return answer