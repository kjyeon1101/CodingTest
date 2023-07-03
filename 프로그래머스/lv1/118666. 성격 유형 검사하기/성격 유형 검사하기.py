def solution(survey, choices):
    answer = ''
    kbti = {
        'R':0, 'T':0,
        'C':0, 'F':0,
        'J':0, 'M':0,
        'A':0, 'N':0
    }
    
    for s, c in zip(survey, choices):
        if c > 4:
            kbti[s[1]] += (c - 4)
        elif c < 4:
            kbti[s[0]] += (4 - c)

    answer += 'R' if kbti['R'] >= kbti['T'] else 'T'
    answer += 'C' if kbti['C'] >= kbti['F'] else 'F'
    answer += 'J' if kbti['J'] >= kbti['M'] else 'M'
    answer += 'A' if kbti['A'] >= kbti['N'] else 'N'

    return answer