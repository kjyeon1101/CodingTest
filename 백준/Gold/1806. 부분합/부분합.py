import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
sums = []
s = 0
for n in numbers:
  s += n
  sums += [s]

p1 = 0
p2 = 0
answer = N+1
while p1 < N:
  if p2 < N:
    if p1 == 0:
      tmp = sums[p2]
    else:
      tmp = sums[p2] - sums[p1-1]
    if tmp >= S:
      answer = min(answer, p2-p1+1)
      p1 += 1
    else:
      p2 += 1
  else:
    p1 += 1
if answer == N+1:
  print(0)
else:
  print(answer)