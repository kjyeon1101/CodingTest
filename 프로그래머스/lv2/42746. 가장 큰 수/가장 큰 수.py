def solution(numbers):
    sort_keys = []
    
    for n in numbers:
        n = str(n)
        if len(n) == 1:
            sort_keys.append((n, n[0], n[0], n[0], n[0]))
        elif len(n) == 2:
            sort_keys.append((n, n[0], n[1], n[0], n[1]))
        elif len(n) == 3:
            sort_keys.append((n, n[0], n[1], n[2], n[0]))
        else:
            sort_keys.append((n, n[0], n[1], n[2], n[3]))
    
    sort_keys = sorted(sort_keys, key=lambda x:(x[1],x[2],x[3],x[4], -len(x[0])), reverse=True)
    answer = "".join([s[0] for s in sort_keys])
    
    if answer[0] == "0":
        return "0"
    
    return answer