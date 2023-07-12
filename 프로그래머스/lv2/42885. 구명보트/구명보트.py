def solution(people, limit):
    answer = 0
    people = sorted(people, reverse=True)
    heavy = 0
    light = len(people)-1
    
    while True:
        if people[heavy] + people[light] <= limit:
            heavy += 1
            light -= 1
        else:
            heavy += 1
            
        answer += 1
        
        if heavy > light:
            break
        
    return answer