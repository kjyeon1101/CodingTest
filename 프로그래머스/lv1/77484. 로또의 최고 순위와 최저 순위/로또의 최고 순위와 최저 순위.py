def solution(lottos, win_nums):
    l = len(set(win_nums) & set(lottos))
    answer = [min(7 - (lottos.count(0) + l), 6), min(7 - l, 6)]
    return answer