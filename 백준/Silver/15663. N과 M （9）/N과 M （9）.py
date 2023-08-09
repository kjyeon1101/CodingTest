import sys
input = sys.stdin.readline

from itertools import permutations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
perm = sorted(list(set(permutations(numbers, M))))
for p in perm:
  print((" ".join([str(a) for a in p])).strip())