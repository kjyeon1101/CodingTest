import sys
input = sys.stdin.readline

import heapq

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
heap = []
INF = 1e8
distance = [INF for _ in range(V+1)]
for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u].append((v,w))

distance[K] = 0
heapq.heappush(heap, (0, K))
while heap:
  dist, node = heapq.heappop(heap)
  if dist > distance[node]:
    continue
  for next, weight in graph[node]:
    if dist + weight < distance[next]:
      distance[next] = dist + weight
      heapq.heappush(heap, (distance[next], next))

for d in distance[1:]:
  if d == INF:
    print("INF")
  else:
    print(d)