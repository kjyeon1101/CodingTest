def solution(price, money, count):
    S = count*(2*price+(count-1)*price)/2
    answer = S - money if S - money > 0 else 0
    return answer