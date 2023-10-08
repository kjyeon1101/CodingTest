import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    direct = [0,1,2,3]
    r, c, d = map(int, input().split()) # d=0북,1동,2남,3서
    room = [] # 0=아직청소안한빈칸, 1=벽, 2=청소한빈칸
    for _ in range(N):
        room.append(list(map(int, input().split())))
    
    dr = [-1,0,1,0] # 북 동 남 서
    dc = [0,1,0,-1]
    while True:
        if room[r][c] == 0: # 현재칸이 청소되지 않았으면
            room[r][c] = 2 # 청소
        
        flag = False
        for i in range(4): # 상하좌우칸 확인
            nextr = r + dr[i]
            nextc = c + dc[i]
            if nextr < 1 or nextr >= N-1 or nextc < 1 or nextc >= M-1:
                continue
            if room[nextr][nextc] == 0: # 청소되지 않은 빈칸 존재
                flag = True
                break

        if flag: # 청소되지 않은 빈칸 있음
            d = direct[d-1] # 반시계 90도 회전
            if room[r+dr[d]][c+dc[d]] == 0:
                r += dr[d] # 바라보는 방향으로 앞으로 한칸 전진
                c += dc[d]
        else: # 모두 청소 or 벽
            r += dr[direct[d-2]] # 바라보는 방향 유지, 한칸 후진
            c += dc[direct[d-2]]
            if room[r][c] == 1: # 후진했더니 벽 (멈춤)
                break

    answer = 0
    for r in room:
        answer += r.count(2)
    print(answer)
    return

if __name__ == "__main__":
    solution()