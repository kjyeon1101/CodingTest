def solution(x):
    if x % sum([int(i) for i in str(x)]) == 0:
        return True
    else:
        return False