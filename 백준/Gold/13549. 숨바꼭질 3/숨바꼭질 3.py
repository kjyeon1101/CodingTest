import sys
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())
queue = deque([(N, 0)])
visited = [False] * 100001
visited[N] = True

while queue:
  now, time = queue.popleft()
  if now == K:
    print(time)
    break
  for next, second in [(now*2, time), (now-1, time+1), (now+1, time+1)]:
    if 0 <= next <= 100000 and visited[next] == False:
      queue.append((next, second))
      visited[next] = True