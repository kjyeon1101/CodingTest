import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = 1e8
distance = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
  distance[i][i] = 0
  
for _ in range(m):
  a, b, c = map(int, input().split())
  distance[a][b] = min(c, distance[a][b])

for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      distance[i][j] = min(distance[i][k]+distance[k][j], distance[i][j])

for dist in distance[1:]:
  for d in dist[1:]:
    if d == INF:
      print(0, end=' ')
    else:
      print(d, end=' ')
  print()