def solution(dartResult):
    answer = 0
    stack = []
    dartResult = dartResult.replace("10", "A")
    sdt = {"S":1, "D":2, "T":3}
    
    for d in dartResult:
        if d == '*':
            # 마지막으로 들어간 2개 뽑아서 2배씩
            l1 = stack.pop() * 2
            if len(stack) > 0:
                l2 = stack.pop() * 2
                stack.append(l2)
            stack.append(l1)
        elif d == '#':
            # 마지막으로 들어간 1개 뽑아서 -1배
            l = stack.pop() * -1
            stack.append(l)
        elif d.isalpha():
            # 마지막으로 들어간 1개 뽑아서 제곱
            if d == 'A':
                stack.append(10)
            else:
                l = stack.pop() ** sdt[d]
                stack.append(l)
        else:
            # 스택에 넣기
            stack.append(int(d))
            
    answer = sum(stack)
    return answer