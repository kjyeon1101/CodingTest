def solution(s):
    answer = 0
    idx = 0
    a = 0
    b = 0
    
    for i, w in enumerate(s):
        if w == s[idx]:
            a += 1
        else:
            b += 1
        if a == b:
            answer += 1
            idx = i + 1
            a = 0
            b = 0
            
    if len(s[idx:idx+a+1]) > 0:
        answer += 1
        
    return answer