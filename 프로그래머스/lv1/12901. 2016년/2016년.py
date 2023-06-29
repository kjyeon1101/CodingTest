def solution(a, b):
    month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    for i in range(1,a):
        b += month[i]
    answer = week[b%7]
    return answer