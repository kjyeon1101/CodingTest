import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    
    for s in scoville:
        heapq.heappush(heap, s)

    while heap[0] < K and len(heap) >= 2:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        if a == 0 and b == 0:
            return -1
        heapq.heappush(heap, a+b*2)
        answer += 1
    
    if heap[0] < K:
        return -1
        
    return answer