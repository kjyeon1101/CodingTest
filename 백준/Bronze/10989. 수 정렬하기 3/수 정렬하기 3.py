import sys
input = sys.stdin.readline

N = int(input())

cnt = [0 for i in range(100001)]
for _ in range(N):
  n = int(input())
  cnt[n] += 1

for i, c in enumerate(cnt):
  if c > 0:
    for _ in range(c):
      print(i)