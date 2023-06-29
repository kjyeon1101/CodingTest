def solution(name, yearning, photo):
    answer = []
    for pho in photo:
        answer.append(sum([yearning[name.index(p)] if p in name else 0 for p in pho]))
    return answer