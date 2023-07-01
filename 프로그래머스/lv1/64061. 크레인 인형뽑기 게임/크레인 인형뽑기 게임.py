from collections import deque

def solution(board, moves):
    answer = 0
    l = len(board)
    get_stack = deque()
    brd_stack = [[0 for i in range(l)] for j in range(l)]
    
    for i in range(l):
        for j in range(l):
            brd_stack[i][j] = board[j][i]
        while brd_stack[i].count(0) > 0:
            brd_stack[i].remove(0)

    for m in moves:
        if len(brd_stack[m-1]) > 0:
            p = brd_stack[m-1].pop(0)
            if len(get_stack) > 0:
                top = get_stack.pop()
                if top != p:
                    get_stack += [top, p]
                else:
                    answer += 2
            else:
                get_stack.append(p)

    return answer