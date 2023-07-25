import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []

for _ in range(N):
  board.append(input())

white_board = []
black_board = []
for i in range(N):
  row = []
  if i % 2 == 0:
    if M % 2 == 0:
      white_row = ["W", "B"] * (M // 2)
      black_row = ["B", "W"] * (M // 2)
    else:
      white_row = ["W", "B"] * (M // 2) + ["W"]
      black_row = ["B", "W"] * (M // 2) + ["B"]
  else:
    if M % 2 == 0:
      white_row = ["B", "W"] * (M // 2)
      black_row = ["W", "B"] * (M // 2)
    else:
      white_row = ["B", "W"] * (M // 2) + ["B"]
      black_row = ["W", "B"] * (M // 2) + ["W"]
  white_board.append(white_row)
  black_board.append(black_row)

for i in range(N):
  for j in range(M):
    if board[i][j] != white_board[i][j]:
      white_board[i][j] = 1
    else:
      white_board[i][j] = 0
    if board[i][j] != black_board[i][j]:
      black_board[i][j] = 1
    else:
      black_board[i][j] = 0

min_cnt = 2500
for i in range(N-7):
  for j in range(M-7):
    white_cnt = 0
    black_cnt = 0
    for row in white_board[i:i+8]:
      white_cnt += row[j:j+8].count(1)
    for row in black_board[i:i+8]:
      black_cnt += row[j:j+8].count(1)
    min_cnt = min(min_cnt, white_cnt, black_cnt)

print(min_cnt)