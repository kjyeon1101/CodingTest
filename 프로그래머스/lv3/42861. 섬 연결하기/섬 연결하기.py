def solution(n, costs):
    answer = 0
    visited = [False for i in range(n)]
    index = 0
    goto = []
    
    while visited.count(False) > 0:
        visited[index] = True
        goto += [(cost[0], cost[1], cost[2]) for cost in costs if cost[0] == index or cost[1] == index]
        goto = sorted(list(set(goto)), key=lambda x:x[2])
        
        for g in goto:
            if visited[g[0]] == False:
                index = g[0]
                answer += g[2]
                break
            elif visited[g[1]] == False:
                index = g[1]
                answer += g[2]
                break
    
    return answer