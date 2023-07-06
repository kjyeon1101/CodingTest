def solution(prices):
    answer = [0 for i in range(len(prices))]
    stack = []
    
    for i, p in enumerate(prices):
        while len(stack) > 0 and stack[-1][1] > p:
            t = stack.pop()
            answer[t[0]] = i - t[0]
        stack.append((i, p))
    
    for s in stack:
        answer[s[0]] = len(prices) - s[0] -1
        
    return answer