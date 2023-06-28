def solution(arr):
    answer = [arr[0]]
    i = 0
    for a in arr:
        if answer[i] != a:
            answer.append(a)
            i += 1
    return answer