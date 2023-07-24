num = int(input())
answer = 0

for i in range(1, num):
  s = i
  for j in list(str(i)):
    s += int(j)
  if s == num:
    answer = i
    break

print(answer)