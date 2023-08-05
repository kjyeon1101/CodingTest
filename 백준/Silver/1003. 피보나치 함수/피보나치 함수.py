import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  # 1 : (n-1)
  n_1_zero = 0
  n_1_one = 1
  # 0 : (n-2)
  n_2_zero = 1
  n_2_one = 0

  zero_cnt = 1
  one_cnt = 1

  if n == 0:
    zero_cnt = 1
    one_cnt = 0
  elif n == 1:
    zero_cnt = 0
    one_cnt = 1
  else:
    for _ in range(2, n+1):
      zero_cnt = n_1_zero + n_2_zero
      one_cnt = n_1_one + n_2_one
      n_2_zero = n_1_zero
      n_1_zero = zero_cnt
      n_2_one = n_1_one
      n_1_one = one_cnt

  print(zero_cnt, one_cnt)