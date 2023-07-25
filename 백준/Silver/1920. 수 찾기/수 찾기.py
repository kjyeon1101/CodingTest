import sys
input = sys.stdin.readline

N = int(input())
N_numbers = list(map(int, input().split()))
M = int(input())
M_numbers = list(map(int, input().split()))

N_numbers.sort()

for m in M_numbers:
  start = 0
  end = N-1
  answer = 0
  
  while start <= end:
    mid = (start + end) // 2
    if N_numbers[mid] == m:
      answer = 1
      break
    elif N_numbers[mid] < m:
      start = mid + 1
    else:
      end = mid - 1

  print(answer)