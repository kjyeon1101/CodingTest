import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
answer = 0

while N > 0:
  half = 2**(N-1)
  # 1사분면
  if r < half and c < half:
    answer += 0
  # 2사분면
  elif r < half and c >= half:
    answer += half * half
    c -= half
  # 3사분면
  elif r >= half and c < half:
    answer += half * half * 2
    r -= half
  # 4사분면
  elif r >= half and c >= half:
    answer += half * half * 3
    r -= half
    c -= half
  N -= 1

print(answer)