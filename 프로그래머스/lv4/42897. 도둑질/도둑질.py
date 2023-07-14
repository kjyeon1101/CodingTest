def solution(money):
    s1 = [m for m in money]
    s2 = [m for m in money]
    
    s1[1] = s1[0]
    for i in range(2, len(money)-1):
        s1[i] = max(s1[i-1], s1[i-2]+s1[i])
    
    s2[0] = 0
    for i in range(2, len(money)):
        s2[i] = max(s2[i-1], s2[i-2]+s2[i])
    
    answer = max(s1[-2], s2[-1])
    return answer