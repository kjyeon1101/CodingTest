import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
  row = list(map(int, input().split()))
  board.append(row)

s_list = [[0 for _ in range(N)] for _ in range(N)]
for i, row in enumerate(board):
  s = 0
  for j, r in enumerate(row):
    s += r
    if i == 0:
      s_list[i][j] = s
    else:
      s_list[i][j] = s + s_list[i-1][j]

for _ in range(M):
  x1, y1, x2, y2 = map(lambda x:int(x)-1, input().split())
  answer = s_list[x2][y2]
  if x1-1 >= 0:
    answer -= s_list[x1-1][y2]
  if y1-1 >= 0:
    answer -= s_list[x2][y1-1]
  if x1-1 >= 0 and y1-1 >= 0:
    answer += s_list[x1-1][y1-1]
  print(answer)