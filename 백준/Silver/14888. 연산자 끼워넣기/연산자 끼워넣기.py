import sys
input = sys.stdin.readline

def dfs(depth, answer):
    global N, A_list, maximum, minimum, plus, minus, multiply, divide

    if depth == N:
        maximum = max(maximum, answer)
        minimum = min(minimum, answer)
        return

    if plus > 0:
        plus -= 1
        dfs(depth+1, answer + A_list[depth])
        plus += 1
    if minus > 0:
        minus -= 1
        dfs(depth+1, answer - A_list[depth])
        minus += 1
    if multiply > 0:
        multiply -= 1
        dfs(depth+1, answer * A_list[depth])
        multiply += 1
    if divide > 0:
        divide -= 1
        dfs(depth+1, int(answer / A_list[depth]))
        divide += 1

    return

def solution():
    global N, A_list, maximum, minimum, plus, minus, multiply, divide
    N = int(input())
    A_list = list(map(int, input().split()))
    plus, minus, multiply, divide = map(int, input().split())
    maximum = -1000000000
    minimum = 1000000000
    answer = A_list[0]
    dfs(1, answer)
    print(maximum)
    print(minimum)


if __name__ == '__main__':
    solution()