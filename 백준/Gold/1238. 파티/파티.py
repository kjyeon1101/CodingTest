import sys
input = sys.stdin.readline

import heapq

def dijkstra(graph, node):
  distance = [1e8 for _ in range(len(graph))]
  distance[node] = 0
  heap = []
  heapq.heappush(heap, (0, node))
  while heap:
    dist, now = heapq.heappop(heap)
    for next, weight in graph[now]:
      if dist + weight < distance[next]:
        distance[next] = dist + weight
        heapq.heappush(heap, (distance[next], next))
  return distance[1:]

N, M, X = map(int, input().split())
roads = [[] for _ in range(N+1)]
for _ in range(M):
  s, e, t = map(int, input().split())
  roads[s].append((e,t))

distances = []
for i in range(1, N+1):
  distances.append(dijkstra(roads, i))

print(max([distances[i][X-1] + distances[X-1][i] for i in range(N)]))