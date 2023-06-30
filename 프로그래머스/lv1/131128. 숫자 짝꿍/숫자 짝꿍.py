def solution(X, Y):
    s = "".join([i*min(X.count(i), Y.count(i)) for i in set(X) & set(Y)])
    if len(s) > 0:
        if s.count("0") == len(s):
            return "0"
        else:
            return "".join(sorted(s, reverse=True))
    else:
        return "-1"