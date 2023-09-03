from sys import stdin
from math import inf

N = int(stdin.readline())
board = []

for _ in range(N):
    board.append([int(x) for x in stdin.readline().split()])

costs = [[0] * (1 << N) for _ in range(N + 1)]

def get_min_cost(cnt, visited):
    if visited == (2 ** N - 1):
        if board[cnt][0]:
            return board[cnt][0]
        return inf

    if costs[cnt][visited]:
        return costs[cnt][visited]

    left_cost = inf

    for c in range(N):
        if not (visited & (1 << c)) and board[cnt][c]:
            temp = board[cnt][c] + get_min_cost(c, visited + (1 << c))
            left_cost = min(left_cost, temp)

    costs[cnt][visited] = left_cost
    return left_cost

print(get_min_cost(0, 1))