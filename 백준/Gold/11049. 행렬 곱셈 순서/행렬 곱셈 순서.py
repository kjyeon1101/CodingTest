import sys
input = sys.stdin.readline

N = int(input())
matrix = []
for _ in range(N):
    a, b = map(int, input().split())
    matrix.append((a,b))
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(1, N):
    for j in range(N-i):
        row = j
        col = j + i
        if i == 1:
            dp[row][col] = matrix[row][0] * matrix[row][1] * matrix[col][1]
        else:
            dp[row][col] = 2**32
            for k in range(row, col):
                dp[row][col] = min(dp[row][col], dp[row][k] + dp[k+1][col] + matrix[row][0] * matrix[k][1] * matrix[col][1])
print(dp[0][-1])