def solution(t, p):
    answer = 0
    i = 0
    while i <= len(t)-len(p):
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1
        i += 1
        
    return answer