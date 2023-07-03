def solution(ingredient):
    answer = 0
    burger_stack = []
    for i in ingredient:
        burger_stack.append(i)
        if len(burger_stack) >= 4:
            if burger_stack[-4:] == [1,2,3,1]:
                burger_stack.pop()
                burger_stack.pop()
                burger_stack.pop()
                burger_stack.pop()
                answer += 1
    return answer