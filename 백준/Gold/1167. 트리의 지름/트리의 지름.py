import sys
input = sys.stdin.readline

from collections import deque

V = int(input())
tree = [[] for _ in range(V+1)]
for _ in range(V):
  edges = list(map(int, input().split()))
  node = edges[0]
  for i in range(1, len(edges)-2, 2):
    tree[node].append((edges[i], edges[i+1]))

queue = deque([(1,0)])
visited = [False] * (V+1)
visited[1] = True
max = [-1, -1]

for _ in range(2):
  while queue:
    now, dist = queue.popleft()
    if dist > max[1]:
      max[0] = now
      max[1] = dist
    for next, weight in tree[now]:
      if not visited[next]:
        queue.append((next, dist+weight))
        visited[next] = True
  queue.append((max[0], 0))
  visited = [False] * (V+1)
  visited[max[0]] = True
  
print(max[1])