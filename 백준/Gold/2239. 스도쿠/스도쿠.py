import sys
input = sys.stdin.readline

def possible_numbers(i,j):
  return [l for l in range(1,10) if row_check[i][l] and col_check[j][l] and box_check[(i//3)*3+j//3][l]]

def backtracking(k):
  if k >= len(zero):
    for row in board:
      print("".join(map(str, row)))
    exit()
    
  i = zero[k][0]
  j = zero[k][1]

  for p in possible_numbers(i,j):
    board[i][j] = p
    row_check[i][p] = False
    col_check[j][p] = False
    box_check[(i//3)*3+j//3][p] = False
    backtracking(k+1)
    board[i][j] = 0
    row_check[i][p] = True
    col_check[j][p] = True
    box_check[(i//3)*3+j//3][p] = True

board = []
for _ in range(9):
  row = input().strip()
  board.append([int(r) for r in row])
  
zero = []
row_check = [[True]*10 for _ in range(9)]
col_check = [[True]*10 for _ in range(9)]
box_check = [[True]*10 for _ in range(9)]

for i in range(9):
  for j in range(9):
    if board[i][j] == 0:
      zero.append((i,j))
    else:
      row_check[i][board[i][j]] = False
      col_check[j][board[i][j]] = False
      box_check[(i//3)*3+j//3][board[i][j]] = False
      
backtracking(0)