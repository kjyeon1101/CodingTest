num = int(input())

bee = 0
s = 1
answer = 1

while True:
  s += bee
  if s >= num:
    break
  bee += 6
  answer += 1
  
print(answer)