import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
s = 0
s_list = []
for n in numbers:
  s += n
  s_list.append(s)

for _ in range(M):
  a, b = map(int, input().split())
  if a == 1:
    print(s_list[b-1])
  else:
    print(s_list[b-1]-s_list[a-2])