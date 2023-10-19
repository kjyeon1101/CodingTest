from collections import deque

def bfs(start_r, start_c):
    global ground, N, L, R, visited
    queue = deque()
    visited[start_r][start_c] = True
    queue.append((start_r, start_c))
    dr = [-1,0,1,0]
    dc = [0,-1,0,1]
    union = []
    union.append((start_r,start_c))
    population = ground[start_r][start_c]
    flag = False
    while queue:
        now_r, now_c = queue.popleft()
        for i in range(4):
            next_r = now_r + dr[i]
            next_c = now_c + dc[i]
            if next_r < 0 or next_r >= N or next_c < 0 or next_c >= N:
                continue
            if visited[next_r][next_c] == False and L <= abs(ground[now_r][now_c]-ground[next_r][next_c]) <= R:
                union.append((next_r, next_c))
                population += ground[next_r][next_c]
                visited[next_r][next_c] = True
                queue.append((next_r, next_c))
                flag = True
    if len(union) > 1:
        new_population = population // len(union)
        for r,c in union:
            ground[r][c] = new_population
    return flag

N, L, R = map(int, input().split())
ground = []
for _ in range(N):
    ground.append(list(map(int, input().split())))

days = 0
while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                if bfs(i,j) == True:
                    flag = True
    if flag == False:
        break
    days += 1

print(days)