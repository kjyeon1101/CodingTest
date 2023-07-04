def solution(park, routes):
    answer = []
    X = []
    
    for i, pa in enumerate(park):
        for j, p in enumerate(pa):
            if p == 'X':
                X.append((i,j))
            elif p == 'S':
                S = (i,j)
    
    for r in routes:
        op = r.split()[0]
        n = int(r.split()[1])
        
        if op == "N":
            move_to = (S[0]-n, S[1])
            pass_list = [(i, S[1]) for i in range(move_to[0], S[0])]
        elif op == "S":
            move_to = (S[0]+n, S[1])
            pass_list = [(i, S[1]) for i in range(S[0]+1, move_to[0]+1)]
        elif op == "W":
            move_to = (S[0], S[1]-n)
            pass_list = [(S[0], i) for i in range(move_to[1], S[1])]
        elif op == "E":
            move_to = (S[0], S[1]+n)
            pass_list = [(S[0], i) for i in range(S[1]+1, move_to[1]+1)]

        if move_to[0] < 0 or move_to[0] >= len(park) or move_to[1] < 0 or move_to[1] >= len(park[0]):
            continue

        if len(set(pass_list) & set(X)) > 0:
            continue
        
        S = move_to
        
    answer = [S[0], S[1]]
    return answer