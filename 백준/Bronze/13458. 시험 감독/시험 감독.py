N = int(input())
A_list = list(map(int, input().split()))
B, C = map(int, input().split())
answer = 0

for a in A_list:
    answer += 1 # 총감독관
    a -= B
    if a > 0: # 부감독관 필요
        tmp = a // C
        answer += tmp
        a -= tmp * C
        if a > 0:
            answer += 1

print(answer)