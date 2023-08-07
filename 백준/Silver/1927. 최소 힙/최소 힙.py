import sys
input = sys.stdin.readline

import heapq

N = int(input())
heap = []
for _ in range(N):
  x = int(input())
  if x == 0:
    if len(heap) > 0:
      print(heapq.heappop(heap))
    else:
      print(0)
  else:
    heapq.heappush(heap, x)