import sys
input = sys.stdin.readline

n = int(input())
m = n*0.15
if m - int(m) < 0.5:
  m = int(m)
else:
  m = int(m) + 1
  
level_count = [0] * 31
for _ in range(n):
  l = int(input())
  level_count[l] += 1

levels = []
for i in range(31):
  if level_count[i] != 0:
    levels += [i] * level_count[i]

if n > 0:
  answer = sum(levels[m:n-m])/len(levels[m:n-m])
  if answer - int(answer) < 0.5:
    answer = int(answer)
  else:
    answer = int(answer) + 1
  print(answer)
else:
  print(0)