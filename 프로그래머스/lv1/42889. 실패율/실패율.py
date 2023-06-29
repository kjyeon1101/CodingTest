def solution(N, stages):
    answer = []
    stages = sorted(stages, reverse=True)
    fail = []
    
    for i in range(N,0,-1):
        if i in stages:
            challengers = stages.count(i)
            reachers = len(stages[:stages.index(i)]) + challengers
            fail.append(challengers/reachers)
        else:
            fail.append(0)
    fail.reverse()
    
    for i in range(N):
        max_fail_index = fail.index(max(fail))
        answer.append(max_fail_index+1)
        fail[max_fail_index] = -1
        
    return answer