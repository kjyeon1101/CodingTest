N, K = map(int, input().split())
things = [(0,0)]
P = [[0 for _ in range(K+1)] for _ in range(N+1)]
for _ in range(N):
  W, V = map(int, input().split())
  things.append((W,V))

for i in range(1, N+1):
  w = things[i][0]
  v = things[i][1]
  for j in range(1, K+1):
    if w > j:
      P[i][j] = P[i-1][j]
    else:
      P[i][j] = max(P[i-1][j-w] + v, P[i-1][j])

print(P[-1][-1])