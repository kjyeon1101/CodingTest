import sys
input = sys.stdin.readline

def backtracking(k, visited, perm):
    global N
    if k == N+1:
        print(" ".join([str(p) for p in perm]))
        return
    for i in range(1, N+1):
        if visited[i] == False:
            visited[i] = True
            perm.append(i)
            backtracking(k+1, visited, perm)
            perm.pop()
            visited[i] = False
    return

def solution():
    global N
    N = int(input())
    visited = [False for _ in range(N+1)]
    perm = []
    backtracking(1, visited, perm)
    return

if __name__ == '__main__':
    solution()