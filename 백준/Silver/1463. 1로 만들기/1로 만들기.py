import sys
input = sys.stdin.readline

N = int(input())
cnt = [0, 1, 1]

for i in range(4, N+1):
  num = [i - 1]
  if i % 3 == 0:
    num.append(i // 3)
  if i % 2 == 0:
    num.append(i // 2)
  cnt.append(min([cnt[n-1] for n in num]) + 1)

print(cnt[N-1])