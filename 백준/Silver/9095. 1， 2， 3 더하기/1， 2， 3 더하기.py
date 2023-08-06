import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
  count = [1, 2, 4]
  n = int(input())
  for i in range(3, n):
    s = count[i-1] + count[i-2] + count[i-3]
    count.append(s)
  print(count[n-1])