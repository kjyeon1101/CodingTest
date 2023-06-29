def solution(n):
    answer = 0
    for i in range(n):
        answer += 1
        while answer % 3 == 0 or str(answer).find("3") != -1:
            answer += 1
    return answer