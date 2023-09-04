import sys
input = sys.stdin.readline

N = int(input())
list = sorted(list(map(int, input().split())))
s = 3000000000
answer = []
flag = 0
for i in range(N-2):
  cur = i
  start = i+1
  end = N-1
  while start < end:
    sum = list[cur] + list[start] + list[end]
    if abs(sum) < abs(s):
      s = sum
      answer = [list[cur], list[start], list[end]]
      if s == 0:
        flag = 1
        break
    if sum < 0:
      start += 1
    else:
      end -= 1
  if flag:
    break
answer.sort()
for a in answer:
  print(a, end=' ')
print()