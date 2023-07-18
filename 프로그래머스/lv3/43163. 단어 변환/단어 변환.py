from collections import deque

def compare_string(string1, string2, visited):
    same = 0
    diff = 0
    
    if string2 in visited:
        return 0
    
    for s1, s2 in zip(string1, string2):
        if s1 == s2:
            same += 1
        else:
            diff += 1
            
    if diff == 1:
        return 1
    else:
        return 0

def solution(begin, target, words):
    answer = 0
    idx = 1
    queue = deque()
    queue.append((0, begin))
    visited = [begin]

    while queue:
        now = queue.popleft()
        idx = now[0] + 1
        
        if now[1] == target:
            answer = idx - 1
            break
            
        if len(words) <= idx:
            break
            
        for word in words:
            if compare_string(now[1], word, visited):
                queue.append((idx, word))
                visited.append(word)
        
    return answer