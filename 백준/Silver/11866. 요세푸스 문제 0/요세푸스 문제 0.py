import sys
input = sys.stdin.readline

N, K = map(int, input().split())
people = [i for i in range(1, N+1)]
yo = []
idx = 0

while people:
  idx += (K-1)
  idx %= len(people)
  yo.append(people.pop(idx))

answer = str(yo).replace("[", "<").replace("]", ">")
print(answer)