def solution(strings, n):
    string_dict = dict()
    for s in strings:
        string_dict[s] = s[n]
    string_dict = sorted(string_dict.items(), key=lambda x:(x[1], x[0]))
    answer = [i[0] for i in string_dict]
    return answer