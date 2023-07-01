def solution(participant, completion):
    par = dict()
    for p in participant:
        if p in par.keys():
            par[p] += 1
        else:
            par[p] = 1
            
    for c in completion:
        par[c] -= 1
            
    answer = [p for p in par if par[p] == 1][0]
    return answer