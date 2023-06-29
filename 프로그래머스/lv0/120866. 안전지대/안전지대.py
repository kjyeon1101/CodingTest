def solution(board):
    n = len(board)
    danger = set()
    
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j] == 1:
                danger.update([(i+x,j+y) for x in [-1,0,1] for y in [-1,0,1]])
    
    count = 0
    for a,b in danger:
        if 0 <= a < len(board) and 0 <= b < len(board):
            count += 1
            
    answer = n*n - count
    
    return answer