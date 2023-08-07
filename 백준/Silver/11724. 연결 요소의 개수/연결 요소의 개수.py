import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
visited[0] = True
for _ in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

answer = 0
while True:
  if visited.count(False) == 0:
    break
  start = visited.index(False)
  stack = [start]
  while stack:
    top = stack.pop()
    if visited[top] == False:
      visited[top] = True
      for g in graph[top]:
        if visited[g] == False:
          stack.append(g)
  answer += 1

print(answer)