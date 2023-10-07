import sys
input = sys.stdin.readline
import heapq

def solution():
    N, M, K, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
    INF = 1e8
    distance = [INF for _ in range(N+1)]
    distance[X] = 0
    heap = []
    heapq.heappush(heap, (0,X))

    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for next_city in graph[now]:
            if distance[next_city] > dist + 1:
                distance[next_city] = dist + 1
                heapq.heappush(heap, (distance[next_city], next_city))
    
    if K in distance:
        for i in range(1, N+1):
            if distance[i] == K:
                print(i)
    else:
        print(-1)
    return

if __name__ == "__main__":
    solution()