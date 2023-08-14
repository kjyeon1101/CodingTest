import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
  parent, child, weight = map(int, input().split())
  graph[parent].append((child,weight))
  graph[child].append((parent,weight))

queue = deque([(1,0)])
visited = [False] * (N+1)
visited[1] = True
max = [-1,-1]

for _ in range(2):
  while queue:
    now, dist = queue.popleft()
    if dist > max[1]:
      max[0] = now
      max[1] = dist
    for next, weight in graph[now]:
      if visited[next] == False:
        queue.append((next, dist + weight))
        visited[next] = True
  queue.append((max[0], 0))
  visited = [False] * (N+1)
  visited[max[0]] = True

print(max[1])