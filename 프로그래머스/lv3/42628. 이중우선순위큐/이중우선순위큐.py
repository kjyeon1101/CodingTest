import heapq

def solution(operations):
    min_heap = []
    
    for op in operations:
        o, n = op.split()
        n = int(n)
        
        if o == "I":
            heapq.heappush(min_heap, n)
        else:
            if len(min_heap) > 0:
                if n == -1:
                    heapq.heappop(min_heap)
                else:
                    min_heap.remove(max(min_heap))

    if len(min_heap) == 0:
        return [0, 0]
    else:
        return [max(min_heap), min_heap[0]]