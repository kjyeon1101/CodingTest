def solution(s):
    answer = []
    for i, a in enumerate(s):
        if a in s[:i][::-1]:
            answer.append(s[:i][::-1].index(a)+1)
        else:
            answer.append(-1)
    return answer