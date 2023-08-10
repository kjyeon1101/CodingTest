import sys
input = sys.stdin.readline

n = int(input())
triangle = []
for _ in range(n):
  row = list(map(int, input().split()))
  triangle.append(row)

triangle.reverse()
for i, tri in enumerate(triangle[1:]):
  for j, t in enumerate(tri):
    triangle[i+1][j] += max(triangle[i][j], triangle[i][j+1])

print(triangle[-1][0])