import sys
input = sys.stdin.readline

def sand_move(r,c,next_r,next_c):
    if r == next_r and c-next_c == 1:
        # print("왼쪽")
        sand_fly = [(next_r-2,next_c,0.02),(next_r-1,next_c-1,0.1),(next_r-1,next_c,0.07),(next_r-1,next_c+1,0.01),(next_r,next_c-2,0.05),(next_r+1,next_c-1,0.1),(next_r+1,next_c,0.07),(next_r+1,next_c+1,0.01),(next_r+2,next_c,0.02),(next_r,next_c-1,0.55)]
        sand_fly_func(sand_fly,next_r,next_c)
    elif c == next_c and next_r-r == 1:
        # print("아래")
        sand_fly = [(next_r-1,next_c-1,0.01),(next_r-1,next_c+1,0.01),(next_r,next_c-2,0.02),(next_r,next_c-1,0.07),(next_r,next_c+1,0.07),(next_r,next_c+2,0.02),(next_r+1,next_c-1,0.1),(next_r+1,next_c+1,0.1),(next_r+2,next_c,0.05),(next_r+1,next_c,0.55)]
        sand_fly_func(sand_fly,next_r,next_c)
    elif r == next_r and next_c-c == 1:
        # print("오른쪽")
        sand_fly = [(next_r-2,next_c,0.02),(next_r-1,next_c-1,0.01),(next_r-1,next_c,0.07),(next_r-1,next_c+1,0.1),(next_r,next_c+2,0.05),(next_r+1,next_c-1,0.01),(next_r+1,next_c,0.07),(next_r+1,next_c+1,0.1),(next_r+2,next_c,0.02),(next_r,next_c+1,0.55)]
        sand_fly_func(sand_fly,next_r,next_c)
    else:
        # print("위")
        sand_fly = [(next_r-2,next_c,0.05),(next_r-1,next_c-1,0.1),(next_r-1,next_c+1,0.1),(next_r,next_c-2,0.02),(next_r,next_c-1,0.07),(next_r,next_c+1,0.07),(next_r,next_c+2,0.02),(next_r+1,next_c-1,0.01),(next_r+1,next_c+1,0.01),(next_r-1,next_c,0.55)]
        sand_fly_func(sand_fly,next_r,next_c)

def sand_fly_func(sand_fly,nr,nc):
    global out_sand
    cnt = 0
    for r,c,ratio in sand_fly[:-1]:
        sand = int(A[nr][nc] * ratio)
        cnt += sand
        if 0 <= r < N and 0 <= c < N:
            A[r][c] += sand
        else:
            out_sand += sand
    r,c,ratio = sand_fly[-1]
    if 0 <= r < N and 0 <= c < N:
        A[r][c] += (A[nr][nc]-cnt)
    else:
        out_sand += (A[nr][nc]-cnt)
    A[nr][nc] = 0

N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

r = N//2
c = N//2
out_sand = 0

dt = 1
while dt <= N:
    # print(f"태풍 현재 위치 : ({r},{c})")
    if dt % 2 == 1: # 홀수 : 왼쪽 -> 아래
        # 왼쪽
        next_r = r
        for i in range(1,dt+1):
            next_c = c-1
            # print(f"태풍 : ({r},{c})->({next_r},{next_c})")
            sand_move(r,c,next_r,next_c)
            c = c-1
            if dt == N and i == dt-1:
                break
        if dt == N:
            break
        # 아래
        next_c = c
        for i in range(1,dt+1):
            next_r = r+1
            # print(f"태풍 : ({r},{c})->({next_r},{next_c})")
            sand_move(r,c,next_r,next_c)
            r = r+1
    else: # 짝수 : 오른쪽 -> 위
        # 오른쪽
        next_r = r
        for i in range(1,dt+1):
            next_c = c+1
            # print(f"태풍 : ({r},{c})->({next_r},{next_c})")
            sand_move(r,c,next_r,next_c)
            c = c+1
        # 위
        next_c = c
        for i in range(1,dt+1):
            next_r = r-1
            # print(f"태풍 : ({r},{c})->({next_r},{next_c})")
            sand_move(r,c,next_r,next_c)
            r = r-1
    dt += 1

print(out_sand)