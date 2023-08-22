import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
for _ in range(T):
  N, K = map(int, input().split())
  D_list = [0]
  D_list += list(map(int, input().split()))
  graph = [[] for _ in range(N+1)]
  indegree = [0 for _ in range(N+1)]
  dp = [-1 for _ in range(N+1)]
  for _ in range(K):
    X, Y = map(int, input().split())
    graph[X].append(Y)
    indegree[Y] += 1
  W = int(input())

  queue = deque()
  for i in range(1, N+1):
    if indegree[i] == 0:
      queue.append(i)
      dp[i] = D_list[i]
  
  while queue:
    now = queue.popleft()
    if now == W:
      break
    for g in graph[now]:
      indegree[g] -= 1
      if indegree[g] == 0:
        queue.append(g)
      dp[g] = max(dp[g], dp[now]+D_list[g])

  print(dp[W])