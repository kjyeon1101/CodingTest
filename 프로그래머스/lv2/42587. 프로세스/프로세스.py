from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    
    for i, p in enumerate(priorities):
        queue.append((i,p))
    
    while len(queue) > 0:
        max_priority = max([q[1] for q in queue])
        process = queue.popleft()
        
        if process[1] < max_priority:
            queue.append(process)
        else:
            answer += 1
            if process[0] == location:
                return answer
        