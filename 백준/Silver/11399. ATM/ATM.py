import sys
input = sys.stdin.readline

N = int(input())
P = sorted(list(map(int, input().split())))

s = 0
answer = 0
for p in P:
  s += p
  answer += s
print(answer)