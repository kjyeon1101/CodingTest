import sys
input = sys.stdin.readline
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for g in graph[v]:
        if not visited[g]:
            dfs(graph, g, visited)

def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for g in graph[now]:
            if not visited[g]:
                queue.append(g)
                visited[g] = True

def solution():
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s, d = map(int, input().split())
        graph[s].append(d)
        graph[d].append(s)
    for i in range(1,N+1):
        graph[i].sort()

    visited = [False for _ in range(N+1)]
    dfs(graph, V, visited)
    print()

    visited = [False for _ in range(N+1)]
    bfs(graph, V, visited)
    print()

    return

if __name__ == "__main__":
    solution()