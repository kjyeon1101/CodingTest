import sys
input = sys.stdin.readline

def subsequence(start):
  global answer

  if len(seq) > 0 and sum(seq) == S:
    answer += 1

  for i in range(start, N):
    seq.append(numbers[i])
    subsequence(i+1)
    seq.pop()

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0
seq = []

subsequence(0)
print(answer)