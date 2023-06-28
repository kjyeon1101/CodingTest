def solution(sizes):
    for i, s in enumerate(sizes):
        sizes[i] = sorted(s)
    answer = max([sizes[i][0] for i in range(len(sizes))]) * max([sizes[i][1] for i in range(len(sizes))])
    return answer