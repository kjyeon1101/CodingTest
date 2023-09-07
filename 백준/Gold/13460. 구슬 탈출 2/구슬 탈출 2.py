import sys
input = sys.stdin.readline
from collections import deque

def left(now_x,now_y,other_x,other_y):
    # 현재위치 (now_x,now_y)
    # 이동할위치 (now_x,1)
    x = now_x
    y = now_y
    for i in range(now_y-1, 0, -1):
        y = i
        # 구멍 => 거기서 멈춤
        if board[x][y] == "O":
            break
        # 벽이나 다른공 => 그 옆에서 멈춤
        elif board[x][y] == "#" or (x==other_x and y==other_y):
            y += 1
            break
    return x, y

def right(now_x,now_y,other_x,other_y):
    # 현재위치 (now_x,now_y)
    # 이동할위치 (now_x,M-2)
    x = now_x
    y = now_y
    for i in range(now_y, M-1):
        y = i
        # 구멍 => 거기서 멈춤
        if board[x][y] == "O":
            break
        # 벽이나 다른공 => 그 옆에서 멈춤
        if board[x][y] == "#" or (x==other_x and y==other_y):
            y -= 1
            break
    return x, y

def up(now_x,now_y,other_x,other_y):
    # 현재위치 (now_x,now_y)
    # 이동할위치 (1,now_y)
    x = now_x
    y = now_y
    for i in range(now_x-1, 0, -1):
        x = i
        # 구멍 => 거기서 멈춤
        if board[x][y] == "O":
            break
        # 벽이나 다른공 => 그 옆에서 멈춤
        if board[x][y] == "#" or (x==other_x and y==other_y):
            x += 1
            break
    return x, y

def down(now_x,now_y,other_x,other_y):
    # 현재위치 (now_x,now_y)
    # 이동할위치 (N-2,now_y)
    x = now_x
    y = now_y
    for i in range(now_x, N-1):
        x = i
        # 구멍 => 거기서 멈춤
        if board[x][y] == "O":
            break
        # 벽이나 다른공 => 그 옆에서 멈춤
        if board[x][y] == "#" or (x==other_x and y==other_y):
            x -= 1
            break
    return x, y

N, M = map(int, input().split())
board = []
red = [0,0]
blue = [0,0]
hole = [0,0]
for i in range(N):
    board.append([char for char in input().strip()])
    for j in range(M):
        if board[i][j] == "R":
            red[0] = i
            red[1] = j
        elif board[i][j] == "B":
            blue[0] = i
            blue[1] = j
        elif board[i][j] == "O":
            hole[0] = i
            hole[1]= j
    
queue = deque()
queue.append([0,red,blue])
x_direct = [-1,0,1,0]
y_direct = [0,-1,0,1]
visited = []

while queue:
    depth, nr, nb = queue.popleft()
    # print(f"depth={depth}, red={nr}, blue={nb}, hole={hole}")
    if depth == 11:
        print(-1)
        break
    if (nr[0] == hole[0] and nr[1] == hole[1]) and (nb[0] != hole[0] or nb[1] != hole[1]): # 빨간구슬만 구멍에 빠진 경우
        print(depth)
        break
    elif nb[0] == hole[0] and nb[1] == hole[1]: # 파란구슬이 구멍에 빠진 경우
        continue
    for i in range(4):
        x = x_direct[i]
        y = y_direct[i]
        if i == 0: # 왼쪽
            # 왼쪽에 있는거부터
            if nr[1] < nb[1]:
                red_next_x, red_next_y = left(nr[0], nr[1], nb[0], nb[1])
                blue_next_x, blue_next_y = left(nb[0], nb[1], red_next_x, red_next_y)
            else:
                blue_next_x, blue_next_y = left(nb[0], nb[1], nr[0], nr[1])
                red_next_x, red_next_y = left(nr[0], nr[1], blue_next_x, blue_next_y)
        elif i == 1: # 오른쪽
            # 오른쪽에 있는거부터
            if nr[1] > nb[1]:
                red_next_x, red_next_y = right(nr[0], nr[1], nb[0], nb[1])
                blue_next_x, blue_next_y = right(nb[0], nb[1], red_next_x, red_next_y)
            else:
                blue_next_x, blue_next_y = right(nb[0], nb[1], nr[0], nr[1])
                red_next_x, red_next_y = right(nr[0], nr[1], blue_next_x, blue_next_y)
        elif i == 2: # 위쪽
            # 위쪽에 있는거부터
            if nr[0] < nb[0]:
                red_next_x, red_next_y = up(nr[0], nr[1], nb[0], nb[1])
                blue_next_x, blue_next_y = up(nb[0], nb[1], red_next_x, red_next_y)
            else:
                blue_next_x, blue_next_y = up(nb[0], nb[1], nr[0], nr[1])
                red_next_x, red_next_y = up(nr[0], nr[1], blue_next_x, blue_next_y)
        else: # 아래쪽
            # 아래쪽에 있는거부터
            if nr[0] > nb[0]:
                red_next_x, red_next_y = down(nr[0], nr[1], nb[0], nb[1])
                blue_next_x, blue_next_y = down(nb[0], nb[1], red_next_x, red_next_y)
            else:
                blue_next_x, blue_next_y = down(nb[0], nb[1], nr[0], nr[1])
                red_next_x, red_next_y = down(nr[0], nr[1], blue_next_x, blue_next_y)

        coor = [[red_next_x, red_next_y],[blue_next_x, blue_next_y]]
        if coor not in visited:
            queue.append([depth+1]+coor)
            visited.append(coor)
else:
    print(-1)