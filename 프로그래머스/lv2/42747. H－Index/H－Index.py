def solution(citations):
    answer = 0
    n = len(citations)
    citations = sorted(citations)
    count = [citations.count(i) for i in range(0,citations[n-1]+1)]
    
    for h in range(n, -1, -1):
        if sum(count[h:]) >= h and h > answer:
            answer = h
            
    return answer