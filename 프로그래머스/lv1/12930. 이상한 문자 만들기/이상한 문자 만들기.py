def solution(s):
    index = 0
    s_list = list(s)
    for i, w in enumerate(s):
        if w != ' ':
            if index % 2 == 0:
                s_list[i] = s[i].upper()
            else:
                s_list[i] = s[i].lower()
            index += 1
        else:
            index = 0
            
    answer = "".join(s_list)
    return answer