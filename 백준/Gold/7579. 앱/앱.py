import sys
input = sys.stdin.readline
from math import inf

N, M = map(int, input().split())
m_list = [0] + list(map(int, input().split()))
c_list = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(sum(c_list)+1)] for _ in range(N+1)]
answer = inf

for i in range(1, N+1):
    for j in range(len(dp[0])):
        if c_list[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c_list[i]]+m_list[i])
        if dp[i][j] >= M:
            answer = min(answer ,j)

print(answer)