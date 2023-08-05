import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n_people = []
m_people = []
for _ in range(N):
  n_people.append(input().strip())
for _ in range(M):
  m_people.append(input().strip())

answer = set(n_people) & set(m_people)
print(len(answer))
for a in sorted(list(answer)):
  print(a)