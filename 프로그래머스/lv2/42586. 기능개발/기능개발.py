from collections import deque
from math import ceil

def solution(progresses, speeds):
    answer = []
    queue = deque()
    
    for p, s in zip(progresses, speeds):
        queue.append(ceil((100 - p) / s))
    
    while len(queue) > 0:
        b = queue.popleft()
        a = 1
        while len(queue) > 0 and queue[0] <= b:
            queue.popleft()
            a += 1
        answer.append(a)
    
    return answer