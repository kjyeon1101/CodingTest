def solution(babbling):
    answer = 0
    
    for bab in babbling:
        bab = bab.replace("aya", "A")
        bab = bab.replace("ye", "Y")
        bab = bab.replace("woo", "W")
        bab = bab.replace("ma", "M")

        if bab.isupper():
            if len(bab) > 1:
                prev = bab[0]
                for b in bab[1:]:
                    if prev == b:
                        break
                    prev = b
                else:
                    answer += 1
            else:
                answer += 1
                
    return answer