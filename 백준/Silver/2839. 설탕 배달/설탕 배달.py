import sys
input = sys.stdin.readline

N = int(input())
answer = 0

while N:
  if N % 5 != 0:
    N -= 3
    if N < 0:
      answer = -1
    answer += 1
  else:
    answer += (N // 5)
    N = 0

print(answer)