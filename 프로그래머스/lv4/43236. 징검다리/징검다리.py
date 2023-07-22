def solution(distance, rocks, n):
    answer = 0
    start = 0
    end = distance
    rocks = [start] + sorted(rocks) + [end]

    while start <= end:
        mid = (start + end) // 2
        intervals = [rocks[i+1]-rocks[i] for i, r in enumerate(rocks[:-1])]
        cnt = 0
        for i, interval in enumerate(intervals):
            if interval < mid and i < len(intervals) - 1:
                cnt += 1
                intervals[i+1] += interval
                intervals[i] = 0
            elif interval < mid and i == len(intervals) - 1:
                cnt += 1
                intervals[i-1] += interval
                intervals[i] = 0
        if cnt > n:
            end = mid - 1
        elif cnt <= n:
            answer = mid
            start = mid + 1
        
    return answer