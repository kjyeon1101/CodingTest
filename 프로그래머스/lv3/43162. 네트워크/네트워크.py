def dfs(graph, v, visited):
    visited[v] = True
    for i, g in enumerate(graph[v]):
        if g == 1 and i != v and visited[i] == False:
            dfs(graph, i, visited)

def solution(n, computers):
    answer = 0
    visited = [False] * len(computers)
    idx = 0
    
    while True:
        dfs(computers, idx, visited)
        answer += 1
        if visited.count(False) > 0:
            idx = visited.index(False)
        else:
            break

    return answer