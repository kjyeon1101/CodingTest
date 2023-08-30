import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
questions = []
for _ in range(M):
  S, E = map(int, input().split())
  questions.append((S,E))
  
dp = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
  for j in range(i+1):
    if i == j:
      dp[i][j] = 1
    elif i == j + 1:
      if numbers[i] == numbers[j]:
        dp[i][j] = 1
    else:
      if numbers[i] == numbers[j] and dp[i-1][j+1] == 1:
        dp[i][j] = 1
  
for s, e in questions:
  print(dp[e-1][s-1])