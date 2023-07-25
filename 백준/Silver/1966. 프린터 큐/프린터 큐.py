import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
testcases= []

for _ in range(T):
  N, M = map(int, input().split())
  priority = [(i,p)for i, p in enumerate(list(map(int, input().split())))]
  testcases.append([N,M,priority])

for testcase in testcases:
  N = testcase[0]
  M = testcase[1]
  priority = testcase[2]

  queue = deque(priority)
  answer = 0
  
  while queue:
    now = queue.popleft()
  
    for q in queue:
      if now[1] < q[1]:
        queue.append(now)
        break
    else:
      answer += 1
      if now[0] == M:
        break

  print(answer)