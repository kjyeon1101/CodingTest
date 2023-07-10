def solution(brown, yellow):
    answer = []
    for y in range(1, int(yellow**0.5)+1):
        if yellow % y == 0:
            x = yellow // y
            if (x+2) * (y+2) == brown + yellow:
                answer = [x+2, y+2]
                break
    return answer