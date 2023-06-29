def solution(n, m, section):
    answer = 0
    while len(section) > 0:
        end = section[0] + m - 1
        while len(section) > 0 and section[0] <= end:
            section.pop(0)
        answer += 1
    return answer