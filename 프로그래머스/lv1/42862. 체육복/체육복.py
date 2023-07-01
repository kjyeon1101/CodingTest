def solution(n, lost, reserve):
    res = list(set(reserve) - set(lost))
    los = list(set(lost) - set(reserve))

    for i in range(1,n+1):
        if i in los:
            if i-1 in res:
                los.remove(i)
                res.remove(i-1)
            elif i+1 in res:
                los.remove(i)
                res.remove(i+1)

    answer = n - len(los)
    return answer