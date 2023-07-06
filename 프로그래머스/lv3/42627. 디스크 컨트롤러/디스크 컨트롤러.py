import heapq

def solution(jobs):
    answer = 0
    time = 0
    l = len(jobs)
    heap = []
    
    while len(heap) > 0 or len(jobs) > 0:
        for j in jobs[:]:
            if j[0] <= time:
                heapq.heappush(heap, (j[1], j[0]))
                jobs.remove(j)
        
        if len(heap) > 0:
            work = heapq.heappop(heap)
            time += work[0]
            answer += time - work[1]
        else:
            time += 1
    
    return answer // l