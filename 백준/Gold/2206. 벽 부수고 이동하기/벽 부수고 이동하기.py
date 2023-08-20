from collections import deque

N, M = map(int, input().split())
board = []
visited = [[[False for _ in range(2)] for _ in range(M)] for _ in range(N)]
# visited[row][col][0] = 벽 부수지 않은 경우
# visited[row][col][1] = 벽 부순 경우
for _ in range(N):
  row = input().strip()
  tmp = []
  for r in row:
    tmp.append(int(r))
  board.append(tmp)

queue = deque()
queue.append((0,0,0,0))
visited[0][0][0] = True

while queue:
  row, col, dist, wall = queue.popleft()
  if row == N-1 and col == M-1:
    print(dist+1)
    break
  nexts = [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]
  for next_row, next_col in nexts:
    if 0 <= next_row < N and 0 <= next_col < M:
      # 범위 안에 있을 때
      if board[next_row][next_col] == 0: # 빈칸
        if wall == 0: # 아직 안부숨
          if visited[next_row][next_col][0] == False:
            queue.append((next_row, next_col, dist+1, wall))
            visited[next_row][next_col][0] = True
        else: # 부숨
          if visited[next_row][next_col][1] == False:
            queue.append((next_row, next_col, dist+1, wall))
            visited[next_row][next_col][1] = True
      else:
        if wall == 0: # 벽
          # 아직 안부숨
          if visited[next_row][next_col][0] == False:
            queue.append((next_row, next_col, dist+1, 1))
            visited[next_row][next_col][0] = True
          if visited[next_row][next_col][1] == False:
            queue.append((next_row, next_col, dist+1, 1))
            visited[next_row][next_col][1] = True
else:
  print("-1")