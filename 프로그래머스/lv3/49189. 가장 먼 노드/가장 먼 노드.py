import heapq

def solution(n, edge):
    INF = 1e8
    distance = [INF] * (n + 1)
    distance[0] = -1
    distance[1] = 0
    heap = []
    heapq.heappush(heap, (distance[1], 1))
    graph = [[] for _ in range(n+1)]
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    while heap:
        now = heapq.heappop(heap)
        
        if distance[now[1]] < now[0]:
            continue

        for g in graph[now[1]]:
            if now[0] + 1 < distance[g]:
                distance[g] = now[0] + 1
                heapq.heappush(heap, (distance[g], g))
                
    answer = distance.count(max(distance))
    return answer