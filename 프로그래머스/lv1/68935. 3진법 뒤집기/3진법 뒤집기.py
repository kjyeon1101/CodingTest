def solution(n):
    answer = 0
    n3 = []
    
    while n > 0:
        n3.append(n%3)
        n //= 3
    
    n3.reverse()
    for i, n in enumerate(n3):
        answer += n * 3**i
        
    return answer