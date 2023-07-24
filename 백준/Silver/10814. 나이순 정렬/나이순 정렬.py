import sys
input = sys.stdin.readline

N = int(input())
people = []

for i in range(N):
  age, name = input().split()
  people.append((i, int(age), name))

people = sorted(people, key=lambda x:(x[1], x[0]))

for p in people:
  print(p[1], p[2])