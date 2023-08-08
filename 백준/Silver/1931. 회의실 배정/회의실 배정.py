import sys
input = sys.stdin.readline

N = int(input())
meetings = []
for _ in range(N):
  start, end = map(int, input().split())
  meetings.append((start, end))
meetings = sorted(meetings, key=lambda x:(x[1], x[0]))

answer = 1
time = meetings[0][1]

for start, end in meetings[1:]:
  if start >= time:
    time = end
    answer += 1

print(answer)