import sys
input = sys.stdin.readline

def check(i,j,p):
  if p in board[i]:
    return False
  elif p in [board[k][j] for k in range(9)]:
    return False
  else:
    x = (i//3) * 3
    y = (j//3) * 3
    for a in range(3):
      for b in range(3):
        if p == board[x+a][y+b]:
          return False
  return True

def backtracking(k):
  if k >= len(zero):
    for row in board:
      print("".join([str(b) for b in row]))
    exit()
    
  i = zero[k][0]
  j = zero[k][1]

  for p in range(1,10):
    if check(i,j,p):
      board[i][j] = p
      backtracking(k+1)
      board[i][j] = 0


board = []
for _ in range(9):
  row = input().strip()
  board.append([int(r) for r in row])
zero = [(i,j) for i in range(9) for j in range(9) if board[i][j] == 0]
backtracking(0)