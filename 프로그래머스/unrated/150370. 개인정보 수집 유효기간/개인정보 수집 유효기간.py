def solution(today, terms, privacies):
    answer = []
    terms_dict = dict()
    today = list(map(int, today.split(".")))
    todays = today[0] * 12 * 28 + today[1] * 28 + today[2]
    
    for term in terms:
        t = term.split()
        terms_dict[t[0]] = int(t[1])
    
    for i, privacy in enumerate(privacies):
        start_date = list(map(int, privacy.split()[0].split(".")))
        term = privacy.split()[1]
        days = start_date[0] * 12 * 28 + start_date[1] * 28 + start_date[2] + terms_dict[term] * 28
        
        if todays - days >= 0:
            answer.append(i+1)
        
    return sorted(answer)