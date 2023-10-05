import sys
input = sys.stdin.readline

def roll_dice(cmd):
    global dice
    d1,d2,d3,d4,d5,d6 = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]
    if cmd == 1: # 동쪽
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = d4,d2,d1,d6,d5,d3
    elif cmd == 2: # 서쪽
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = d3,d2,d6,d1,d5,d4
    elif cmd == 3: # 북쪽
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = d5,d1,d3,d4,d6,d2
    elif cmd == 4: # 남쪽
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = d2,d6,d3,d4,d1,d5
    return

def solution():
    global dice
    N, M, x, y, K = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    command = list(map(int, input().split()))
    dice = [0 for _ in range(6)]

    for c in command:
        if c == 1 and y < M-1: # 동쪽
            y += 1
        elif c == 2 and y > 0: # 서쪽
            y -= 1
        elif c == 3 and x > 0: # 북쪽
            x -= 1
        elif c == 4 and x < N-1: # 남쪽
            x += 1
        else:
            continue
        roll_dice(c)
        if board[x][y] == 0:
            board[x][y] = dice[5]
        else:
            dice[5] = board[x][y]
            board[x][y] = 0
        print(dice[0])
    return

if __name__ == '__main__':
    solution()