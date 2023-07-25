import sys
input = sys.stdin.readline

T = int(input())
brackets = []
for _ in range(T):
  brackets.append(input().strip())

for bracket in brackets:
  stack = []
  for b in bracket:
    if b == '(':
      stack.append(b)
    else:
      if len(stack) > 0 and stack[-1] == '(':
        stack.pop()
      else:
        stack.append(b)

  if len(stack) == 0:
    print("YES")
  else:
    print("NO")