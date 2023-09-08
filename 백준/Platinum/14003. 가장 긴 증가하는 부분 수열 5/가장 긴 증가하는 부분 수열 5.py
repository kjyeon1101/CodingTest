import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
numbers = list(map(int, input().split()))
lis = [numbers[0]]
dp = [(0,numbers[0])]

for i in range(1,N):
    if numbers[i] > lis[-1]:
        lis.append(numbers[i])
        dp.append((len(lis)-1, numbers[i]))
    else:
        idx = bisect_left(lis, numbers[i])
        lis[idx] = numbers[i]
        dp.append((idx, numbers[i]))

L = len(lis)
lastIdx = L - 1
answer = []
for i in range(N-1,-1,-1):
    if dp[i][0] == lastIdx:
        answer.append(dp[i][1])
        lastIdx -= 1

print(L)
for a in answer[::-1]:
    print(a, end=' ')
print()