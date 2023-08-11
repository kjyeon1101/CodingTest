import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()
lcs = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]

for i in range(len(str1)):
  for j in range(len(str2)):
    if str1[i] == str2[j]:
      lcs[i+1][j+1] = lcs[i][j] + 1
    else:
      lcs[i+1][j+1] = max(lcs[i+1][j], lcs[i][j+1])

print(lcs[-1][-1])