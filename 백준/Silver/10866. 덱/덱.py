import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
commands = []
for _ in range(N):
  commands.append(input().strip())

deque = deque()

for command in commands:
  c = command.split()
  if c[0] == "push_front":
    deque.appendleft(int(c[1]))
  elif c[0] == "push_back":
    deque.append(int(c[1]))
  elif c[0] == "pop_front":
    if len(deque) > 0:
      print(deque.popleft())
    else:
      print("-1")
  elif c[0] == "pop_back":
    if len(deque) > 0:
      print(deque.pop())
    else:
      print("-1")
  elif c[0] == "size":
    print(len(deque))
  elif c[0] == "empty":
    if len(deque) == 0:
      print("1")
    else:
      print("0")
  elif c[0] == "front":
    if len(deque) > 0:
      print(deque[0])
    else:
      print("-1")
  elif c[0] == "back":
    if len(deque) > 0:
      print(deque[-1])
    else:
      print("-1")