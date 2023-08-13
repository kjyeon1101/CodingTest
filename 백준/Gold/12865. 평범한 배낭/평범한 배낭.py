import sys
input = sys.stdin.readline

N, K = map(int, input().split())
things = []
P = [[0 for _ in range(K+1)] for _ in range(N+1)]
for _ in range(N):
  W, V = map(int, input().split())
  things.append((W,V))

for i, row in enumerate(P[1:]):
  w = things[i][0]
  v = things[i][1]
  for j, r in enumerate(row[1:]):
    if w > j+1:
      P[i+1][j+1] = P[i][j+1]
    else:
      P[i+1][j+1] = max(P[i][j+1-w] + v, P[i][j+1])

print(P[-1][-1])