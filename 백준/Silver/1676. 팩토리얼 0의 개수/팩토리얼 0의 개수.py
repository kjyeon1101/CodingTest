import sys
input = sys.stdin.readline

from math import factorial

N = int(input())
num = str(factorial(N))[::-1]
answer = 0

for n in num:
  if n == "0":
    answer += 1
  else:
    break
    
print(answer)