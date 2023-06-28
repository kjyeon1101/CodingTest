def solution(s, n):
    small = [i for i in range(97, 123)] * 2
    big = [i for i in range(65, 91)] * 2
    
    s_list = []
    for a in s:
        if 97 <= ord(a) <= 122:
            s_list.append(chr(small[ord(a)+n-97]))
        elif 65 <= ord(a) <= 90:
            s_list.append(chr(big[ord(a)+n-65]))
        else:
            s_list.append(" ")
    
    answer = "".join(s_list);
    return answer