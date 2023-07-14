def solution(m, n, puddles):
    if (m == 1 or n == 1) and len(puddles) > 0:
        return 0
    
    board = []
    for i in range(n):
        row = [0 if [j+1,i+1] in puddles else 1 if i == 0 or j == 0 else -1 for j in range(m)]
        board.append(row)
    
    for i in range(m):
        if board[0][i] == 0:
            for j in range(i+1, m):
                board[0][j] = 0
                
    for i in range(n):
        if board[i][0] == 0:
            for j in range(i+1, n):
                board[j][0] = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == -1:
                board[i][j] = board[i-1][j] + board[i][j-1]
    
    answer = board[n-1][m-1] % 1000000007
    return answer