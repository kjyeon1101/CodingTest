import heapq

def solution(operations):
    heap = []
    
    for op in operations:
        o, n = op.split()
        n = int(n)
        
        if o == "I":
            heapq.heappush(heap, n)
        else:
            if len(heap) > 0:
                if n == -1:
                    heapq.heappop(heap)
                else:
                    heap.remove(max(heap))
                    heapq.heapify(heap)

    if len(heap) == 0:
        return [0, 0]
    else:
        return [max(heap), heap[0]]