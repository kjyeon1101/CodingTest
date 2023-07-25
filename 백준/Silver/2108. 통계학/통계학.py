import sys
input = sys.stdin.readline

from collections import Counter

N = int(input())
numbers = []
for _ in range(N):
  numbers.append(int(input()))
numbers.sort()

a1 = sum(numbers) / N
if a1 >= 0:
  if abs(a1 - int(a1)) < 0.5:
    a1 = int(a1)
  else:
    a1 = int(a1) + 1
else:
  if abs(a1 - int(a1)) < 0.5:
    a1 = int(a1)
  else:
    a1 = int(a1) - 1

a2 = numbers[N//2]

c = sorted(Counter(numbers).items(), key=lambda x:(-x[1], x[0]))
a3 = c[0][0]
if len(c) > 1 and c[0][1] == c[1][1]:
  a3 = c[1][0]

a4 = numbers[N-1] - numbers[0]

print(a1)
print(a2)
print(a3)
print(a4)