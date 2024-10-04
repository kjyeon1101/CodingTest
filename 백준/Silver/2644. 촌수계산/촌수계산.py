import sys
from collections import deque
input = sys.stdin.readline

answer = -1
n = int(input())
graph = [[] for _ in range(n+1)]
p1, p2 = map(int, input().split())
m = int(input())

for _ in range(m):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

queue = deque()
visited = [False] * (n+1)
queue.append((p1,0))
while queue:
    now,chonsu = queue.popleft()
    if now == p2:
        answer = chonsu
        break
    visited[now] = True
    for g in graph[now]:
        if not visited[g]:
            queue.append((g,chonsu+1))

print(answer)