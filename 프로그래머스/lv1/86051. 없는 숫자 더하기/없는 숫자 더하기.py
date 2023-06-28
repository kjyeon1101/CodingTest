def solution(numbers):
    all_numbers = {0,1,2,3,4,5,6,7,8,9}
    answer = sum(list(all_numbers-set(numbers)))
    return answer