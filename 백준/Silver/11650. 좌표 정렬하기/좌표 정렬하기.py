import sys
input = sys.stdin.readline

N = int(input())
numbers = []

for _ in range(N):
  x, y = map(int, input().split())
  numbers.append((x, y))

numbers = sorted(numbers, key=lambda x:(x[0], x[1]))

for x, y in numbers:
  print(x, y)