import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

def solution():
    N, M = map(int, input().split())
    board = []
    virus = []
    wall = 0
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(M):
            if row[j] == 2:
                virus.append((i,j))
            elif row[j] == 1:
                wall += 1
        board.append(row)

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    answer = 0
    for x, y, z in list(combinations([(i,j) for i in range(N) for j in range(M) if board[i][j] == 0], 3)):
        queue = deque()
        visited = [[False for _ in range(M)] for _ in range(N)]
        visited[x[0]][x[1]] = True
        visited[y[0]][y[1]] = True
        visited[z[0]][z[1]] = True

        for vx, vy in virus:
            queue.append((vx,vy))
            visited[vx][vy] = True

        while queue:
            nowx, nowy = queue.popleft()
            for i in range(4):
                nextx = nowx + dx[i]
                nexty = nowy + dy[i]
                if nextx < 0 or nextx >= N or nexty < 0 or nexty >= M:
                    continue
                if visited[nextx][nexty] == False and board[nextx][nexty] == 0:
                    queue.append((nextx, nexty))
                    visited[nextx][nexty] = True

        cnt = 0
        for v in visited:
            cnt += v.count(False)
        answer = max(answer, cnt)
    print(answer-wall)

    return

if __name__ == "__main__":
    solution()