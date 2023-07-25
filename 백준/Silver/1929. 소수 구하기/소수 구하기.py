import sys
input = sys.stdin.readline

M, N = map(int, input().split())
chae = [False] * (N + 1)
chae[0] = True
chae[1] = True

for i in range(2, int(N**0.5)+1):
  d = 2
  while i*d <= N:
    chae[i*d] = True
    d += 1

for i, c in enumerate(chae[M:N+1]):
  if c == False:
    print(i+M)