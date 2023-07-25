import sys
input = sys.stdin.readline

T = int(input())
testcase = []

for _ in range(T):
  k = int(input())
  n = int(input())
  testcase.append((k,n))

max_k = max([t[0] for t in testcase])
max_n = max([t[1] for t in testcase])
apart = [[i for i in range(max_n+1)]]

for i in range(1, max_k+1):
  new_row = []
  for j in range(max_n+1):
    new_row.append(sum(apart[i-1][:j+1]))
  apart.append(new_row)

for k, n in testcase:
  print(apart[k][n])