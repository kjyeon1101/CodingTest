def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    i = 0
    while i <= len(score) - m:
        answer += min(score[i:i+m]) * m
        i += m
    return answer