def solution(players, callings):
    order = dict()
    for i, p in enumerate(players):
        order[p] = i
    
    for c in callings:
        c_index = order[c]
        order[c] -= 1
        order[players[c_index - 1]] += 1
        players[c_index - 1], players[c_index] = players[c_index], players[c_index - 1]
    
    answer = players
    return answer