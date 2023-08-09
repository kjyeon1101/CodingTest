import sys
input = sys.stdin.readline

from collections import deque

M, N = map(int, input().split())
tomatoes = []
start = []
visited = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
  row = list(map(int, input().split()))
  tomatoes.append(row)
  for j, r in enumerate(row):
    if r == 1:
      start.append((i,j,0))

if len(start) > 0:
  queue = deque(start)
  visited[start[0][0]][start[0][1]] = True
  answer = 0
  while queue:
    now_r, now_c, now_d = queue.popleft()
    answer = now_d
    for next_r, next_c in [(now_r-1, now_c),(now_r+1, now_c),(now_r, now_c-1),(now_r, now_c+1)]:
      if 0 <= next_r < N and 0 <= next_c < M and tomatoes[next_r][next_c] == 0 and visited[next_r][next_c] == False:
        queue.append((next_r, next_c, now_d+1))
        visited[next_r][next_c] = True
  
  for i, visit in enumerate(visited):
    for j, v in enumerate(visit):
      if v == False and tomatoes[i][j] == 0:
        answer = -1
        break
  
  print(answer)
else:
  print(-1)