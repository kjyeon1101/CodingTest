from collections import Counter

def solution(id_list, report, k):
    report_dict = {i:set() for i in id_list}
    
    for r in report:
        report_dict[r.split()[0]].add(r.split()[1])
    
    report_list = []
    for rv in report_dict.values():
        report_list += list(rv)
    
    stop_list = []
    report_counter = Counter(report_list)
    for c in report_counter:
        if report_counter[c] >= k:
            stop_list.append(c)
    
    answer = [len(report_dict[r] & set(stop_list)) for r in report_dict]
    
    return answer