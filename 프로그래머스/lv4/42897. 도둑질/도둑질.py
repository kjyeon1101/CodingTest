def solution(money):
    l = len(money)
    s1 = [m for m in money]
    s2 = [m for m in money]
    s1[1] = -1
    s2[0] = -1
    s1[2] = s1[0] + s1[2]
    
    for i in range(3, l):
        s1[i] += max(s1[i-2], s1[i-3])
        s2[i] += max(s2[i-2], s2[i-3])

    answer = max(max(s1[l-2], s1[l-3]), max(s2[l-1], s2[l-2]))
    return answer