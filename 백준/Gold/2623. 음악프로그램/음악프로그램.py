import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M):
  orders = list(map(int, input().split()))
  for i in range(1, len(orders)-1):
    graph[orders[i]].append(orders[i+1])
    indegree[orders[i+1]] += 1

queue = deque()
for i in range(1,N+1):
  if indegree[i] == 0:
    queue.append(i)
    indegree[i] -= 1

answer = []
while queue:
  now = queue.popleft()
  answer.append(now)
  for next in graph[now]:
    indegree[next] -= 1
    if indegree[next] == 0:
      queue.append(next)

if len(answer) == N:
  for a in answer:
    print(a)
else:
  print(0)