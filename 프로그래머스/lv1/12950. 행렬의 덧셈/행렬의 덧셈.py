def solution(arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        answer.append([i+j for i,j in zip(a1 ,a2)])
    return answer