import sys
input = sys.stdin.readline

N = int(input())
commands = []
for _ in range(N):
  commands.append(input().strip())

stack = []

for command in commands:
  c = command.split()
  if c[0] == "push":
    stack.append(int(c[1]))
  elif c[0] == "pop":
    if len(stack) > 0:
      print(stack.pop())
    else:
      print("-1")
  elif c[0] == "size":
    print(len(stack))
  elif c[0] == "empty":
    if len(stack) == 0:
      print("1")
    else:
      print("0")
  elif c[0] == "top":
    if len(stack) > 0:
      print(stack[-1])
    else:
      print("-1")