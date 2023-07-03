def solution(s, skip, index):
    answer = ''
    alphabet = sorted(list({'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'} - set(skip)))
    for w in s:
        answer += alphabet[(alphabet.index(w) + index) % len(alphabet)]
    return answer