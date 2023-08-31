import sys
input = sys.stdin.readline
import heapq

N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewels.sort()
bags.sort()

answer = 0
heap = []
i = 0
for b in bags:
  while i < N and jewels[i][0] <= b:
    heapq.heappush(heap, -jewels[i][1])
    i += 1
  if len(heap) > 0:
    v = heapq.heappop(heap)
    answer += (v * -1)
print(answer)