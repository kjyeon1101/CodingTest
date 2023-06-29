def solution(s):
    for i, n in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        s = s.replace(n, str(i))
    return int(s)