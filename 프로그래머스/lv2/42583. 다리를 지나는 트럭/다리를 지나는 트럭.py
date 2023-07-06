from collections import deque

def solution(bridge_length, weight, truck_weights):
    waiting = deque(truck_weights)
    going = deque()
    time = 0
    
    while len(waiting) > 0 or len(going) > 0:
        time += 1
        
        if len(going) > 0 and time - going[0][1] >= bridge_length:
            going.popleft()
            
        if len(waiting) > 0 and waiting[0] + sum([g[0] for g in going]) <= weight:
            w = waiting.popleft()
            going.append((w, time))
    
    return time