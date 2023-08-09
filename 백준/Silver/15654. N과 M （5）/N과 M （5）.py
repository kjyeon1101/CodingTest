import sys
input = sys.stdin.readline

from itertools import permutations

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
for p in permutations(numbers, M):
  print((" ".join([str(a) for a in p])).strip())