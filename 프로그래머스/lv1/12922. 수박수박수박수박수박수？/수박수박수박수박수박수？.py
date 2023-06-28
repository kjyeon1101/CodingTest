def solution(n):
    answer = ''
    soobak = ["수", "박"]
    for i in range(n):
        answer += soobak[i%2]
    return answer