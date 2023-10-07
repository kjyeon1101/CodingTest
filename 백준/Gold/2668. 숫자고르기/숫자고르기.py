import sys
input = sys.stdin.readline

def dfs(graph, v, visited, path):
    global answer
    visited[v] = True
    path.append(v)
    g = graph[v]
    if not visited[g]:
        dfs(graph, g, visited, path)
    else:
        if g in path:
            answer.update(path[path.index(g):])
    return

def solution():
    global answer
    N = int(input())
    numList = [0 for _ in range(N+1)]
    for i in range(1,N+1):
        numList[i] = int(input())
    visited = [False for _ in range(N+1)]
    answer = set()

    for i in range(1,N+1):
        if not visited[i]:
            path = []
            dfs(numList, i, visited, path)

    answer = sorted(list(answer))
    print(len(answer))
    for a in answer:
        print(a)
    return

if __name__ == "__main__":
    solution()