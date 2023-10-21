def backtracking(k):
    global eggs, N, answer
    if k == N: # 가장 오른쪽에 있는 계란
        # print(eggs)
        answer = max(answer, len([e for e in eggs if e[0] <= 0]))
        return
    if eggs[k][0] < 0: # 손에 든 계란이 깨짐
        backtracking(k+1)
    else:
        flag = True
        for i in range(N):
            if i!=k and eggs[i][0] > 0: # 아직 안깨진 계란
                # print(f"{k}번째 계란 들어서 {i}번째 계란이랑 깸")
                eggs[i][0] -= eggs[k][1]
                eggs[k][0] -= eggs[i][1]
                backtracking(k+1)
                eggs[i][0] += eggs[k][1]
                eggs[k][0] += eggs[i][1]
                flag = False
        if flag: # 깨진 계란이 하나도 없음
            backtracking(k+1)
    return

N = int(input())
eggs = []
for _ in range(N):
    s, w = map(int, input().split())
    eggs.append([s,w])
answer = 0
backtracking(0)
print(answer)