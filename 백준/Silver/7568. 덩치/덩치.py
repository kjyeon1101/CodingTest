import sys
input = sys.stdin.readline

N = int(input())
people = []
for _ in range(N):
  w, h = map(int, input().split())
  people.append((w,h))

answer = []
for p1 in people:
  cnt = 0
  for p2 in people:
    if p2[0] > p1[0] and p2[1] > p1[1]:
      cnt += 1
  answer.append(str(cnt + 1))

print(" ".join(answer).strip())