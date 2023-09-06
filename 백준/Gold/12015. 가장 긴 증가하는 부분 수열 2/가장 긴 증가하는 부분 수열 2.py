import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
sequence = list(map(int, input().split()))
lis = [sequence[0]]

for s in range(1,N):
    if lis[-1] < sequence[s]:
        lis.append(sequence[s])
    else:
        idx = bisect_left(lis, sequence[s])
        lis[idx] = sequence[s]
        
print(len(lis))