import sys
input = sys.stdin.readline

def backtracking(start, visited, comb):
    global N, S, answer
    if len(comb) == N//2:
        A = 0
        B = 0
        for i in range(N):
            for j in range(N):
                if visited[i] == True and visited[j] == True:
                    A += S[i][j]
                elif visited[i] == False and visited[j] == False:
                    B += S[i][j]
        answer = min(answer, abs(A-B))
        return
    for i in range(start, N):
        if visited[i] == False:
            visited[i] = True
            comb.append(i)
            backtracking(i+1, visited, comb)
            comb.pop()
            visited[i] = False

def solution():
    global N, S, answer
    N = int(input())
    S = []
    for _ in range(N):
        S.append(list(map(int, input().split())))
    visited = [False for _ in range(N)]
    comb = []
    answer = 1e9
    backtracking(0, visited, comb)
    print(answer)
    return

if __name__ == '__main__':
    solution()