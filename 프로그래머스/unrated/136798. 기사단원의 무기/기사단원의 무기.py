def solution(number, limit, power):
    answer = []
    
    for n in range(1, number+1):
        y = len([i for i in range(1, int(n**0.5)+1) if n % i == 0]) * 2
        if int(n**0.5) == n**0.5:
            y -= 1
        answer.append(y)

    for i, a in enumerate(answer):
        if a > limit:
            answer[i] = power
            
    return sum(answer)