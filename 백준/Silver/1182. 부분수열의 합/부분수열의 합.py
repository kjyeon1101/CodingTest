import sys
input = sys.stdin.readline

def subsequence(k):
  global answer
  if k == len(numbers):
    return
  if sum(seq) == S:
    answer += 1
  for n in range(k+1, len(numbers)):
    if visited[n] == False:
      visited[n] = True
      seq.append(numbers[n])
      subsequence(n)
      seq.pop()
      visited[n] = False

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
visited = [False for _ in range(N)]
answer = 0
for i in range(N):
  seq = []
  seq.append(numbers[i])
  subsequence(i)
print(answer)