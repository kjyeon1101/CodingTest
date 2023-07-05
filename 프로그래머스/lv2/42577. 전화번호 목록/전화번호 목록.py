def solution(phone_book):
    z = {p[:i] for p in phone_book for i in range(1,len(p))}
    for p in phone_book:
        if p in z:
            return False
    return True