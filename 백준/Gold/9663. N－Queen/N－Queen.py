import sys
input = sys.stdin.readline

def backtracking(row): # row행에 놓는 경우
  global N, board, cnt
  if row == N: # 마지막행에 놓았으면
    cnt += 1
    return # 끝
  else: # 중간행
    for col in range(N): # 놓을 수 있는 모든 열에 대해서
      if check(row, col): # row행 col열에 놓을 수 있다면 백트래킹 안하고 마저 진행
        board[row] = col # row행 col열에 퀸 놓고
        backtracking(row+1) # 다음행으로 이동
        board[row] = -1 # 복구(사실 필요없는 과정)
      # (생략) else: row행 col열에 놓을 수 없다면 더이상 진행X 되돌아감, 백트래킹

def check(row, col):
  global board
  for i in range(row): # row행 이전 행들만 봄 (이후는 아직 안놨으니까 볼 필요X)
    if board[i] == col or abs(board[i]-col) == abs(i-row): # 이전행 같은열이나 대각선에 퀸이 이미 있을때는 불가능
      return False
  return True

N = int(input())
cnt = 0
board = [-1 for _ in range(N)] # board[row] = col : row행에는 col열에 놓음
backtracking(0) # 0행부터 놓기 시작
print(cnt)