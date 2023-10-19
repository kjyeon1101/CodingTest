INF = 1e8
N = int(input())
distance = []
for _ in range(N):
    distance.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if distance[i][j] == 0:
            distance[i][j] = INF

for k in range(N):
    for a in range(N):
        for b in range(N):
            distance[a][b] = min(distance[a][b], distance[a][k]+distance[k][b])

for i in range(N):
    for j in range(N):
        if distance[i][j] < INF:
            print("1", end=' ')
        else:
            print("0", end=' ')
    print()