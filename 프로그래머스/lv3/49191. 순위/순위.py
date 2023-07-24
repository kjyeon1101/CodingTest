def solution(n, results):
    answer = 0
    INF = 1e8
    distance = [[INF for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        distance[i][i] = 0
        distance[i][0] = -1
        distance[0][i] = -1
        
    for r in results:
        distance[r[0]][r[1]] = 1
        
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    
    for i, dist in enumerate(distance):
        for j, d in enumerate(dist):
            if distance[i][j] == INF:
                distance[i][j] = -1
        
    for i in range(1,n+1):
        cnt = 0
        for j in range(1,n+1):
            if distance[j][i] > 0:
                cnt += 1
        for d in distance[i]:
            if d > 0:
                cnt += 1
        if cnt == n-1:
            answer += 1
        
    return answer