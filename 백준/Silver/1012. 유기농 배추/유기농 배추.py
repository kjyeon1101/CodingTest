import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(ground, i, j, M, N):
  ground[i][j] = 0
  adjacent = []
  
  if 0 <= i-1 < N and 0 <= j < M:
    adjacent.append((i-1,j))
  if 0 <= i+1 < N and 0 <= j < M:
    adjacent.append((i+1,j))
  if 0 <= i < N and 0 <= j-1 < M:
    adjacent.append((i,j-1))
  if 0 <= i < N and 0 <= j+1 < M:
    adjacent.append((i,j+1))
    
  for a, b in adjacent:
    if ground[a][b] == 1:
      dfs(ground, a, b, M, N)
  
def main():
  T = int(input())
  for _ in range(T):
    M, N, K = map(int, input().split())
    ground = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
      X, Y = map(int, input().split())
      ground[Y][X] = 1

    answer = 0
    for i, row in enumerate(ground):
      for j, r in enumerate(row):
        if r == 1:
          dfs(ground, i, j, M, N)
          answer += 1

    print(answer)

main()