def backtracking(k, num):
    global flag
    if k == N:
        print("".join([str(n) for n in num]))
        flag = True
        return
    for i in range(1,4):
        if check(num+[i]):
            num.append(i)
            backtracking(k+1, num)
            num.pop()
        if flag:
            return
    return

def check(num):
    l = len(num)
    for i in range(1,l//2+1):
        # 확인할 부분수열의 길이 = i
        if num[l-2*i:l-i] == num[l-i:l]:
            return False
    return True

N = int(input())
num = []
flag = False
backtracking(0, num)