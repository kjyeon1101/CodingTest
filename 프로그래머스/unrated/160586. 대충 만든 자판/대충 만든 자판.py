def solution(keymap, targets):
    answer = []
    key_dict = dict()

    for key in keymap:
        for i, k in enumerate(key):
            if k in key_dict.keys():
                key_dict[k] = min(i + 1, key_dict[k])
            else:
                key_dict[k] = i + 1
    
    for tar in targets:
        s = 0
        for t in tar:
            if t in key_dict.keys():
                s += key_dict[t]
            else:
                s = -1
                break
        answer.append(s)
            
    return answer