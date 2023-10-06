import sys
input = sys.stdin.readline

def check():
    global H, ladder
    for k in range(1, N+1):
        now = k
        for h in range(1, H+1):
            if ladder[h][now] == 1:
                now += 1
            elif ladder[h][now] == 2:
                now -= 1
        if now != k:
            return False # k번째 세로선이 k번에 도달하지 않음
    return True

def set_garo(cnt, x, y):
    global ladder, H, N, answer


    if check(): # 정답
        answer = min(answer, cnt)
        return
    elif cnt >= 3 or cnt >= answer:
        return

    for i in range(x, H+1):
        k = y if i == x else 0
        for j in range(k, N):
            if ladder[i][j] == 0 and ladder[i][j+1] == 0:
                # print(f"{j}와 {j+1}을 잇는 사다리를 {i}번째에 놓음")
                ladder[i][j] = 1
                ladder[i][j+1] = 2
                set_garo(cnt+1, i, j+2)
                ladder[i][j] = 0
                ladder[i][j+1] = 0

    return

def solution():
    global H, ladder, N, answer
    N, M, H = map(int, input().split())
    ladder = [[0 for _ in range(N+1)] for _ in range(H+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        ladder[a][b] = 1
        ladder[a][b+1] = 2

    answer = 1e9
    set_garo(0, 1, 1)
    if answer == 1e9:
        print(-1)
    else:
        print(answer)
    return

if __name__ == "__main__":
    solution()