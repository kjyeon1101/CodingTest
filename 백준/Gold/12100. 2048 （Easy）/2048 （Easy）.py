import sys
input = sys.stdin.readline

def find_next_loc(i, j, x, y):
    if i+x < 0 or i+x >= N or j+y < 0 or j+y >= N or board[i+x][j+y] != 0:
        return i, j # 안움직임
    # 움직일 수 있음
    while 0 <= i+x < N and 0 <= j+y < N:
        if board[i+x][j+y] == 0:
            i += x
            j += y
        else:
            break
    return i, j

def backtracking(k):
    global board, answer
    # print(k, board)
    if k == 5:
        m = 0
        for row in board:
            m = max(m, max(row))
        answer = max(answer, m)
        return
    original = []
    for row in board:
        original.append([r for r in row])

    for d in range(4): # 상 좌 하 우
        x = x_direct[d]
        y = y_direct[d]
        comb = []
        combined = [[False for _ in range(N)] for _ in range(N)]
        # 판 변경
        if d == 0: # 상
            for i in range(1,N): # 1행->2행->3행->...->N-1행
                for j in range(N):
                    tmp = board[i][j]
                    if tmp > 0:
                        nextx, nexty = find_next_loc(i,j,x,y)
                        if nextx > 0 and board[nextx-1][nexty] == tmp and combined[nextx-1][nexty] == False: # 합치기
                            nextx -= 1
                            board[nextx][nexty] += tmp
                            combined[nextx][nexty] = True
                        else: # 합치기 X
                            board[nextx][nexty] = tmp
                        if i == nextx and j == nexty:
                            continue
                        board[i][j] = 0
        elif d == 2: # 하
            for i in range(N-2,-1,-1): # N-2행->..->2행->1행->0행
                for j in range(N):
                    tmp = board[i][j]
                    if tmp > 0:
                        nextx, nexty = find_next_loc(i,j,x,y)
                        if nextx < N-1 and board[nextx+1][nexty] == tmp and combined[nextx+1][nexty] == False: # 합치기
                            nextx += 1
                            board[nextx][nexty] += tmp
                            combined[nextx][nexty] = True
                        else: # 합치기 X
                            board[nextx][nexty] = tmp
                        if i == nextx and j == nexty:
                            continue
                        board[i][j] = 0
        elif d == 1: # 좌
            for j in range(1,N): # 1열->2열->3열->...->N-1열
                for i in range(N):
                    tmp = board[i][j]
                    if tmp > 0:
                        nextx, nexty = find_next_loc(i,j,x,y)
                        if nexty > 0 and board[nextx][nexty-1] == tmp and combined[nextx][nexty-1] == False: # 합치기
                            nexty -= 1
                            board[nextx][nexty] += tmp
                            combined[nextx][nexty] = True
                        else: # 합치기 X
                            board[nextx][nexty] = tmp
                        if i == nextx and j == nexty:
                            continue
                        board[i][j] = 0
        else: # 우
            for j in range(N-2,-1,-1): # N-2열->..->2열->1열->0열
                for i in range(N):
                    tmp = board[i][j]
                    if tmp > 0:
                        nextx, nexty = find_next_loc(i,j,x,y)
                        if nexty < N-1 and board[nextx][nexty+1] == tmp and combined[nextx][nexty+1] == False: # 합치기
                            nexty += 1
                            board[nextx][nexty] += tmp
                            combined[nextx][nexty] = True
                        else: # 합치기 X
                            board[nextx][nexty] = tmp
                        if i == nextx and j == nexty:
                            continue
                        board[i][j] = 0
        
        # 백트래킹
        backtracking(k+1)

        # 판 원상복구
        board = []
        for row in original:
            board.append([r for r in row])

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

x_direct = [-1,0,1,0] # 상 좌 하 우
y_direct = [0,-1,0,1] # 상 좌 하 우
combined = [[False for _ in range(N)] for _ in range(N)]
answer = 0
backtracking(0)
print(answer)