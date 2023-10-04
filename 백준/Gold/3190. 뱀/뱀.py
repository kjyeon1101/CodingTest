from collections import deque

N = int(input())
K = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
board[0][0] = 1 # 뱀의 시작위치
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 2 # 사과
L = int(input())
direction = dict()
for _ in range(L):
    l = list(input().split())
    X, C = int(l[0]), l[1]
    direction[X] = C

# print(board)
# print(direction)
snake = deque()
snake.append((0,0))
answer = 0
curr = "right" # 처음에는 오른쪽으로
next_r, next_c = 0, 1
while True:
    # 방향 설정
    if answer in direction.keys(): # 꺾을 차례
        turn = direction[answer]
        if turn == "L": # 왼쪽으로 꺾기
            if curr == "up":
                curr = "left"
            elif curr == "down":
                curr = "right"
            elif curr == "left":
                curr = "down"
            else:
                curr = "up"
        else: # 오른쪽으로 꺾기
            if curr == "up":
                curr = "right"
            elif curr == "down":
                curr = "left"
            elif curr == "left":
                curr = "up"
            else:
                curr = "down"
    
    if curr == "up":
        next_r, next_c = snake[0][0]-1, snake[0][1]
    elif curr == "down":
        next_r, next_c = snake[0][0]+1, snake[0][1]
    elif curr == "left":
        next_r, next_c = snake[0][0], snake[0][1]-1
    else:
        next_r, next_c = snake[0][0], snake[0][1]+1

    if next_r < 0 or next_r >= N or next_c < 0 or next_c >= N: # 범위밖
        answer += 1
        break
    elif board[next_r][next_c] == 1: # 자기자신
        answer += 1
        break
    else:
        snake.appendleft((next_r, next_c))
        if board[next_r][next_c] == 2: # 사과
            board[next_r][next_c] = 1
            answer += 1
            continue
        else: # 빈칸
            tail_r, tail_c = snake.pop()
            board[next_r][next_c] = 1
            board[tail_r][tail_c] = 0

    answer += 1
print(answer)