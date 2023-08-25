import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()
l1 = len(str1)+1
l2 = len(str2)+1
dp = [[0 for _ in range(l2)] for _ in range(l1)]

for i in range(1, l1):
  for j in range(1, l2):
    if str1[i-1] == str2[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])

answer = dp[-1][-1]
print(answer)
if answer > 0:
  lcs = []
  i = l1-1
  j = l2-1
  while dp[i][j] > 0:
    if dp[i-1][j] == dp[i][j]:
      i -= 1
    elif dp[i][j-1] == dp[i][j]:
      j -= 1
    else:
      lcs += str1[i-1]
      i -= 1
      j -= 1
  lcs.reverse()
  print("".join(lcs))