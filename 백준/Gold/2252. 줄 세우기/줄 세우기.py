import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M):
  front, back = map(int, input().split())
  graph[front].append(back)
  indegree[back] += 1

queue = deque()
for i in range(1,N+1):
  if indegree[i] == 0:
    queue.append(i)
    indegree[i] -= 1

while queue:
  now = queue.popleft()
  print(now, end=' ')
  for next in graph[now]:
    indegree[next] -= 1
    if indegree[next] == 0:
      queue.append(next)
print()