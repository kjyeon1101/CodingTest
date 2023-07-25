import sys
input = sys.stdin.readline

from collections import Counter

N, M, B = map(int, input().split())
ground = []
for _ in range(N):
  ground += list(map(int, input().split()))
  
counter_ground = Counter(ground)
a1 = 1e8
a2 = 0
for height in range(min(ground), max(ground)+1):
  block = 0
  time = 0
  
  for h, c in counter_ground.items():
    if h > height:
      block += (h-height) * c
      time += 2 * (h-height) * c
    elif h < height:
      block -= (height-h) * c
      time += 1 * (height-h) * c

  if B+block >= 0:
    if time < a1:
      a1 = time
      a2 = height
    elif time == a1:
      a2 = max(a2, height)

print(a1, a2)