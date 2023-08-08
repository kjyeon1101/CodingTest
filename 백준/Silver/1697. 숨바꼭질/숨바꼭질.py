import sys
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())
queue = deque()
queue.append((N, 0))
visited = [False] * 100001
while queue:
  v, d = queue.popleft()
  visited[v] = True
  if v == K:
    print(d)
    break
  for next in [v-1, v+1, 2*v]:
    if 0 <= next <= 100000 and visited[next] == False:
      queue.append((next, d+1))