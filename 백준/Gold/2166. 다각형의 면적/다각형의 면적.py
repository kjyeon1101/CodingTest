import sys
input = sys.stdin.readline

N = int(input())
coords = []
for _ in range(N):
  x, y = map(int, input().split())
  coords.append((x,y))
coords.append(coords[0])

answer = 0
for i in range(len(coords)-1):
  x1 = coords[i][0]
  y1 = coords[i][1]
  x2 = coords[i+1][0]
  y2 = coords[i+1][1]
  answer += (x1*y2 - x2*y1)
answer = abs(answer) / 2
print(round(answer,1))