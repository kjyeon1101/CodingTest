import sys
input = sys.stdin.readline

from collections import Counter

N = int(input())
N_numbers = list(map(int, input().split()))
M = int(input())
M_numbers = list(map(int, input().split()))

numbers = sorted(Counter(N_numbers).items(), key=lambda x:x[0])

answers = []
for m in M_numbers:
  start = 0
  end = len(numbers) - 1
  answer = 0
  while start <= end:
    mid = (start + end) // 2
    if numbers[mid][0] == m:
      answer = numbers[mid][1]
      break
    elif numbers[mid][0] > m:
      end = mid - 1
    else:
      start = mid + 1
  answers.append(answer)

print(" ".join([str(a) for a in answers]).strip())