def solution(answers):
    answer = [0, 0, 0]
    l = len(answers)
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    s1 = s1 * (l // 5) + s1[:l % 5]
    s2 = s2 * (l // 8) + s2[:l % 8]
    s3 = s3 * (l // 10) + s3[:l % 10]
    
    for a,b,c,d in zip(answers, s1, s2, s3):
        if a == b:
            answer[0] += 1
        if a == c:
            answer[1] += 1
        if a == d:
            answer[2] += 1

    return [i+1 for i, a in enumerate(answer) if a == max(answer)]