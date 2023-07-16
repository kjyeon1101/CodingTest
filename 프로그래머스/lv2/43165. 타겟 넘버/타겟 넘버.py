def solution(numbers, target):
    leaves = [0]
    
    for n in numbers:
        sums = []
        for leaf in leaves:
            sums.append(leaf+n)
            sums.append(leaf-n)
        leaves = sums
    
    answer = leaves.count(target)
    return answer