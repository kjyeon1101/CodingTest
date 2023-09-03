import sys
input = sys.stdin.readline

def dfs(cur, visited):
  if visited == (1 << N) - 1:
    if W[cur][0] != 0:
      return W[cur][0]
    else:
      return INF

  if dp[cur][visited]:
    return dp[cur][visited]

  left = INF
  for next in range(1, N):
    if W[cur][next] == 0:
      continue
    if visited & (1 << next):
      continue
    left = min(left, dfs(next,visited|(1<<next)) + W[cur][next])
  dp[cur][visited] = left
  return dp[cur][visited]

N = int(input())
W = []
INF = 1e9
dp = [[0 for _ in range(1<<N)] for _ in range(N)]
for _ in range(N):
  W.append(list(map(int, input().split())))
print(dfs(0, 1))