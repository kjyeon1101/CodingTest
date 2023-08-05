import sys
input = sys.stdin.readline

def dfs(graph, visited, v):
  if visited[v] == True:
    return
  visited[v] = True
  for g in graph[v]:
    dfs(graph, visited, g)

N = int(input())
M = int(input())
computers = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
  a, b = map(int, input().split())
  computers[a].append(b)
  computers[b].append(a)

dfs(computers, visited, 1)
print(visited.count(True) - 1)