import sys
input = sys.stdin.readline

N = int(input())
rgb = []
for _ in range(N):
  r, g, b = map(int, input().split())
  rgb.append([r,g,b])

i = 0
for r, g, b in rgb[1:]:
  rgb[i+1][0] += min(rgb[i][1], rgb[i][2]) # r
  rgb[i+1][1] += min(rgb[i][0], rgb[i][2]) # g
  rgb[i+1][2] += min(rgb[i][0], rgb[i][1]) # b
  i += 1

print(min(rgb[-1]))