def solution(number, k):
    stack = []
    i = 0
    
    for n in number:
        while len(stack) > 0 and stack[-1] < n and i < k:
            stack.pop()
            i += 1
        stack.append(n)
        
    answer = "".join(stack[:len(number)-k])
    return answer