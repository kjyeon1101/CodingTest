def solution(lines):
    answer = 0
    line_list = []
    line_set = set()
    for line in lines:
        line_list += [(i, i+1) for i in range(line[0], line[1])]
        line_set.update([(i, i+1) for i in range(line[0], line[1])])
    
    for a in line_set:
        if line_list.count(a) > 1:
            answer += 1

    return answer