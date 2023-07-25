import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
queue = deque([i for i in range(1, N+1)])

while len(queue) > 2:
  trash = queue.popleft()
  gotobottom = queue.popleft()
  queue.append(gotobottom)

if len(queue) > 1:
  print(queue[1])
else:
  print(queue[0])