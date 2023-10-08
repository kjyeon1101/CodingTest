import sys
input = sys.stdin.readline

def backtracking(date, total):
    global N, schedule, answer
    endDate = date + schedule[date-1][0]
    if endDate <= N+1:
        answer = max(answer, total)
    else:
        return
    
    for i in range(endDate, N+1):
        if schedule[i-1][0] + i <= N+1:
            total += schedule[i-1][1]
            backtracking(i, total)
            total -= schedule[i-1][1]
    return

def solution():
    global N, schedule,answer
    N = int(input())
    schedule = []
    for _ in range(N):
        T, P = map(int, input().split())
        schedule.append((T,P))
    answer = 0
    for i in range(1,N+1):
        backtracking(i,schedule[i-1][1])
    print(answer)
    return

if __name__ == "__main__":
    solution()