def solution(n, wires):
    answer = n
    
    for i, w in enumerate(wires):
        left_wires = wires[:i] + wires[i+1:]
        S = set(left_wires[0])
        for _ in left_wires:
            for l in left_wires:
                if set(l) & S:
                    S.update(l)
                
        if abs(len(S) - (n - len(S))) < answer:
            answer = abs(len(S) - (n - len(S)))
    
    return answer