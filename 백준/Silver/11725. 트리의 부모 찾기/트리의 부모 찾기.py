import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
queue = deque()
parents = [0 for _ in range(N+1)]
for _ in range(N-1):
  v1, v2 = map(int, input().split())
  graph[v1].append(v2)
  graph[v2].append(v1)

queue.append((1,0))
visited[1] = True
while queue:
  now, parent = queue.popleft()
  parents[now] = parent
  for g in graph[now]:
    if not visited[g]:
      queue.append((g, now))
      visited[g] = True

for p in parents[2:]:
  print(p)