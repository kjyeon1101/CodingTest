import sys
input = sys.stdin.readline

def backtracking(S,idx,depth,k,visited,path):
    if depth == 6:
        print((" ".join([str(p) for p in path])).strip())
        return
    else:
        for i in range(idx,k):
            if not visited[i]:
                visited[i] = True
                path.append(S[i])
                backtracking(S,i,depth+1,k,visited,path)
                path.pop()
                visited[i] = False


while True:
    S = list(map(int, input().split()))
    k = S[0]
    if k == 0:
        break
    S = S[1:]
    visited = [False] * (k+1)
    path = []
    backtracking(S,0,0,k,visited,path)
    print()