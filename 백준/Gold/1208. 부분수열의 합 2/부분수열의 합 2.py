import sys
input = sys.stdin.readline
from itertools import combinations
from bisect import bisect_left, bisect_right

def getSum(nums, sums):
  for i in range(1, len(nums)+1):
    for c in combinations(nums, i):
      sums.append(sum(c))
  sums.sort()

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

left = numbers[:N//2]
right = numbers[N//2:]
left_sum = [0]
right_sum = [0]

getSum(left, left_sum)
getSum(right, right_sum)

answer = 0
for l in left_sum:
  answer += bisect_right(right_sum, S-l) - bisect_left(right_sum, S-l)
  
if S == 0:
  answer -= 1

print(answer)