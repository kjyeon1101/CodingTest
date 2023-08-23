import sys
input = sys.stdin.readline

N = int(input())
sol = list(map(int, input().split()))
p1 = 0
p2 = N-1
s = 2000000000
while p1 < p2:
  mix = sol[p1]+sol[p2]
  if abs(mix) < abs(s):
    answer = [sol[p1], sol[p2]]
    s = mix
  if mix < 0:
    p1 += 1
  else:
    p2 -= 1
print(answer[0], answer[1])