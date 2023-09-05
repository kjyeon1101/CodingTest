import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(k):
    global path
    visited[k] = True
    path += [k]
    next = numbers[k]
    if visited[next] == False:
        dfs(next)
    else:
        if next in path and cycle[next] == False:
            while path:
                p = path.pop()
                cycle[p] = True
                if p == next:
                    break

T = int(input())
for _ in range(T):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    cycle = [False] * (N+1)
    visited = [False] * (N+1)
    for i in range(1,N+1):
        if visited[i] == False and visited[numbers[i]] == False:
            path = []
            dfs(i)
    print(cycle[1:].count(False))