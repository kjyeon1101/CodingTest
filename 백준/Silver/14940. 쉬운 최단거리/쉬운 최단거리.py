import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
ground = []
goal_r = 0
goal_c = 0
queue = deque()
visited = [[False for _ in range(m)] for _ in range(n)]
distance = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
  row = list(map(int, input().split()))
  if 2 in row:
    goal_r = i
    goal_c = row.index(2)
  ground.append(row)

queue.append((goal_r, goal_c, 0))
visited[goal_r][goal_c] = True
while queue:
  now_r, now_c, now_d = queue.popleft()
  distance[now_r][now_c] = now_d
  for next_r, next_c in [(now_r-1,now_c),(now_r+1,now_c),(now_r,now_c-1),(now_r,now_c+1)]:
    if 0 <= next_r < n and 0 <= next_c < m and ground[next_r][next_c] == 1 and visited[next_r][next_c] == False:
      queue.append((next_r, next_c, now_d+1))
      visited[next_r][next_c] = True

for i, visit in enumerate(visited):
  for j, v in enumerate(visit):
    if v == False and ground[i][j] == 1:
      distance[i][j] = -1

for dist in distance:
  print((" ".join([str(d) for d in dist])).strip())