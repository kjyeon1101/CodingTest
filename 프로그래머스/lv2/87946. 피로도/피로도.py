from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for dungeon in permutations(dungeons, len(dungeons)):
        K = k
        n = 0
        for d in dungeon:
            if K >= d[0]:
                K -= d[1]
                n += 1
                
        if n > answer:
            answer = n
            
    return answer