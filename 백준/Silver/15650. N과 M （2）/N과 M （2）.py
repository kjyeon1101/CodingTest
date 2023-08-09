import sys
input = sys.stdin.readline

from itertools import combinations

N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
for c in combinations(numbers, M):
  print((" ".join([str(a) for a in sorted(c)])).strip())