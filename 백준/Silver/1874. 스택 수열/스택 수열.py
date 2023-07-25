import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
queue = deque()
for _ in range(n):
  queue.append(int(input()))

stack = []
answer = []
for i in range(1, n+1):
  stack.append(i)
  answer.append("+")
  while len(stack) > 0 and len(queue) > 0 and stack[-1] == queue[0]:
    stack.pop()
    queue.popleft()
    answer.append("-")

if len(stack) == 0 and len(queue) == 0:
  for a in answer:
    print(a)
else:
  print("NO")