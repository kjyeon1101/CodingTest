def solution(N, number):
    n = []
    
    for i in range(1,9):
        n.append([int(str(N)*i)])
        
        for j,k in zip(range(1,i), range(i-1,0,-1)):
            for nj in n[j-1]:
                for nk in n[k-1]:
                    n[i-1].append(nj+nk)
                    n[i-1].append(nj-nk)
                    n[i-1].append(nj*nk)
                    if nk != 0:
                        n[i-1].append(nj//nk)
                        
            for nk in n[k-1]:
                for nj in n[j-1]:
                    n[i-1].append(nk+nj)
                    n[i-1].append(nk-nj)
                    n[i-1].append(nk*nj)
                    if nj != 0:
                        n[i-1].append(nk//nj)
                        
        n[i-1] = list(set(n[i-1]))
        
        if number in n[i-1]:
            return i

    return -1