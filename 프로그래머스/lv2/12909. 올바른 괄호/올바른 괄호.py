def solution(s):
    stack = []
    
    for g in s:
        if g == '(':
            stack.append(g)
        else:
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(g)
    
    if len(stack) == 0:
        return True
    else:
        return False