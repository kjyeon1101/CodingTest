import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
commands = []
for _ in range(N):
  commands.append(input().strip())

queue = deque()

for command in commands:
  c = command.split()
  if c[0] == "push":
    queue.append(int(c[1]))
  elif c[0] == "pop":
    if len(queue) > 0:
      print(queue.popleft())
    else:
      print("-1")
  elif c[0] == "size":
    print(len(queue))
  elif c[0] == "empty":
    if len(queue) == 0:
      print("1")
    else:
      print("0")
  elif c[0] == "front":
    if len(queue) > 0:
      print(queue[0])
    else:
      print("-1")
  elif c[0] == "back":
    if len(queue) > 0:
      print(queue[-1])
    else:
      print("-1")