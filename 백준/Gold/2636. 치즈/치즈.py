from collections import deque

def bfs(start_r, start_c):
    global visited, N, M, cheeze
    queue = deque()
    queue.append((start_r, start_c))
    visited[start_r][start_c] = True
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    while queue:
        now_r, now_c = queue.popleft()
        for i in range(4):
            next_r = now_r + dr[i]
            next_c = now_c + dc[i]
            if next_r < 0 or next_r >= N-1 or next_c < 0 or next_c >= M-1:
                continue
            if visited[next_r][next_c] == False:
                if cheeze[next_r][next_c] == 0 or cheeze[next_r][next_c] == 2:
                    queue.append((next_r, next_c))
                    visited[next_r][next_c] = True
                elif cheeze[next_r][next_c] == 1:
                    cheeze[next_r][next_c] = 2
                    visited[next_r][next_c] = True
    return

def check():
    global N, M, cheeze
    for i in range(N):
        for j in range(M):
            if cheeze[i][j] == 1:
                return False
    return True

def count():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if cheeze[i][j] == 1:
                cnt += 1
    return cnt

N, M = map(int, input().split())
cheeze = []
for _ in range(N):
    cheeze.append(list(map(int, input().split())))

hour = 0
cnt = 0
while True:
    cnt = count()
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        if visited[i][0] == False: # 왼쪽 변
            bfs(i,0)
        if visited[i][M-1] == False: # 오른쪽 변
            bfs(i,M-1)
    for i in range(M):
        if visited[0][i] == False: # 위쪽 변
            bfs(0,i)
        if visited[N-1][i] == False: # 아래쪽 변
            bfs(N-1,i)
    hour += 1
    if check():
        break

print(hour)
print(cnt)