import sys
input = sys.stdin.readline
from collections import deque

def solution():
    M, N, H = map(int, input().split())
    tomatoes = []
    start = []
    visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
    for i in range(H):
        tomato = []
        for j in range(N):
            row = list(map(int, input().split()))
            for k in range(M):
                if row[k] == 1:
                    start.append((i,j,k))
            tomato.append(row)
        tomatoes.append(tomato)

    queue = deque()
    for s1,s2,s3 in start:
        queue.append((s1,s2,s3,1))
        visited[s1][s2][s3] = True
    
    dx = [1,0,-1,0,0,0] # 오른 왼
    dy = [0,1,0,-1,0,0] # 앞 뒤
    dz = [0,0,0,0,1,-1] # 위 아래

    while queue:
        s1,s2,s3,depth = queue.popleft() # s1=z, s2=y, s3=x
        for i in range(6):
            x = s3 + dx[i]
            y = s2 + dy[i]
            z = s1 + dz[i]
            if x < 0 or x >= M or y < 0 or y >= N or z < 0 or z >= H:
                continue
            if visited[z][y][x] == False and tomatoes[z][y][x] == 0:
                queue.append((z,y,x,depth+1))
                tomatoes[z][y][x] = depth+1
                visited[z][y][x] = True

    cnt = 0
    answer = 0
    for i in range(H):
        for j in range(N):
           cnt += tomatoes[i][j].count(0)
           answer = max(answer, max([t for t in tomatoes[i][j]]))
    if cnt == 0: # 다 익음
        print(answer-1)
    else: # 다 안익음
        print(-1)

if __name__ == "__main__":
    solution()