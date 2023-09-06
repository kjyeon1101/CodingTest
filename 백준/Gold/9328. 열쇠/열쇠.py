import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    building = [["." for _ in range(w+2)]]
    for _ in range(h):
        row = ["."] + [i for i in input().strip()] + ["."]
        building.append(row)
    building.append(["." for _ in range(w+2)])
    keys = [False for _ in range(26)]
    for k in input().strip():
        if k == "0":
            break
        keys[ord(k)-ord('a')] = True
    
    answer = 0
    docs = []
    visited = [[False for _ in range(w+2)] for _ in range(h+2)]
    queue = deque([(0,0)])
    visited[0][0] = True
    while queue:
        nowr, nowc = queue.popleft()
        # print(nowr, nowc)
        for nr, nc in [(nowr+1,nowc),(nowr-1,nowc),(nowr,nowc+1),(nowr,nowc-1)]:
            # 범위밖
            if nr < 0 or nr >= h+2 or nc < 0 or nc >= w+2:
                continue
            # 벽
            if building[nr][nc] == "*":
                continue
            # 이미 방문
            if visited[nr][nc] == True:
                continue

            # 방문하지 않은 빈공간
            if building[nr][nc] == ".":
                queue.append((nr,nc))
                visited[nr][nc] = True
            # 문서
            elif building[nr][nc] == "$":
                # print("문서:",nr,nc)
                # 아직 안주운 문서
                if (nr, nc) not in docs:
                    answer += 1
                    docs.append((nr,nc))
                # 줍든 안줍든 방문
                queue.append((nr,nc))
                visited[nr][nc] = True
            # 문
            elif 'A' <= building[nr][nc] <= 'Z':
                # 열쇠 있음
                if keys[ord(building[nr][nc].lower())-ord('a')]:
                    # print("문열었음:",nr,nc,building[nr][nc])
                    queue.append((nr,nc))
                    visited[nr][nc] = True
                # 열쇠 없음
                else:
                    # print("문 못열었음:",nr,nc,building[nr][nc])
                    continue
            # 아직 안주운 열쇠
            elif 'a' <= building[nr][nc] <= 'z':
                # print("열쇠:",nr,nc,keys)
                # 아직 안주운 열쇠
                if keys[ord(building[nr][nc])-ord('a')] == False:
                    keys[ord(building[nr][nc])-ord('a')] = True
                    visited = [[False for _ in range(w+2)] for _ in range(h+2)]
                # 줍든 안줍든 방문
                queue.append((nr,nc))
                visited[nr][nc] = True

    print(answer)