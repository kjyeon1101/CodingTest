import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    distance = []
    for _ in range(N):
        distance.append(list(map(int, input().split())))
    
    for k in range(N):
        for a in range(N):
            for b in range(N):
                distance[a][b] = min(distance[a][b], distance[a][k]+distance[k][b])

    for _ in range(M):
        A, B, C = map(int, input().split())
        if distance[A-1][B-1] <= C:
            print("Enjoy other party")
        else:
            print("Stay here")
    return

if __name__ == "__main__":
    solution()