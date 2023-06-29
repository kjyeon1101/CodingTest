def solution(n):
    del_nums = {1}
    del_nums.update([i*j for i in range(2, int(n**0.5)+1) for j in range(2, n//i+1)])
    answer = n - len(del_nums)
    return answer