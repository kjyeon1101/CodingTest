num = int(input())
numbers = list(map(int, input().split()))
answer = 0
max_n = max(numbers)
chae = [False] * (max_n + 1)
chae[0] = True
chae[1] = True

for i in range(2, int(max_n**0.5) + 1):
  d = 2
  while i*d <= max_n:
    if chae[i*d] == False:
      chae[i*d] = True
    d += 1

for n in numbers:
  if chae[n] == False:
    answer += 1

print(answer)