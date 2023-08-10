import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  sticker1 = list(map(int, input().split()))
  sticker2 = list(map(int, input().split()))

  dp = [(0, 0, 0)]
  idx = 0
  for s1, s2 in zip(sticker1, sticker2):
    choice1 = max(dp[idx][1], dp[idx][2]) + s1
    choice2 = max(dp[idx][0], dp[idx][2]) + s2
    choice0 = max(dp[idx])
    dp.append((choice1, choice2, choice0))
    idx += 1

  print(max(dp[-1]))