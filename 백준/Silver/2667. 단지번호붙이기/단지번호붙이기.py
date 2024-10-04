import sys
input = sys.stdin.readline

def dfs(map, mx, my, danji):
    map[mx][my] = danji
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for x,y in zip(dx,dy):
        next_x = mx + x
        next_y = my + y
        if 0 <= next_x < N and 0 <= next_y < N and map[next_x][next_y] == 1:
            dfs(map,next_x,next_y,danji)


N = int(input())
map = []
for _ in range(N):
    line = input().strip()
    map.append([int(l) for l in line])

danji = 2
for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            dfs(map,i,j,danji)
            danji += 1

print(danji-2)
cnt_list = []
for i in range(2,danji):
    cnt = 0
    for m in map:
        cnt += m.count(i)
    cnt_list.append(cnt)
for count in sorted(cnt_list):
    print(count)