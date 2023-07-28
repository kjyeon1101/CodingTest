import sys
input = sys.stdin.readline

M = int(input())
S = 0
for _ in range(M):
  command = input().split()
  c = command[0]
  if len(command) > 1:
    x = int(command[1]) - 1
    if c == "add":
      S = S | (1 << x)
    elif c == "remove":
      S = S & ~(1 << x)
    elif c == "check":
      if S & (1 << x):
        print(1)
      else:
        print(0)
    elif c == "toggle":
      S = S ^ (1 << x)
  else:
    if c == "all":
      S = (1 << 20) - 1
    elif c == "empty":
      S = 0