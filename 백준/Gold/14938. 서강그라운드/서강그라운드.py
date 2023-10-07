import sys
input = sys.stdin.readline
import heapq

def solution():
    n, m, r = map(int, input().split())
    item = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    for _ in range(r):
        a, b, l = map(int, input().split())
        graph[a].append((b,l))
        graph[b].append((a,l))
    INF = 1e8
    answer = 0

    for nakha in range(1,n+1):
        distance = [INF for _ in range(n+1)]
        distance[nakha] = 0
        heap = []
        heapq.heappush(heap, (0,nakha))

        while heap:
            dist, now = heapq.heappop(heap)
            if distance[now] < dist:
                continue
            for next_field, weight in graph[now]:
                if dist + weight > m:
                    continue
                if distance[next_field] > dist + weight:
                    distance[next_field] = dist + weight
                    heapq.heappush(heap, (distance[next_field], next_field))

        item_cnt = 0
        for idx in range(1, n+1):
            if distance[idx] < INF:
                item_cnt += item[idx-1]
        answer = max(answer, item_cnt)
        
    print(answer)
    return

if __name__ == "__main__":
    solution()