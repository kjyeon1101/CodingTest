def solution(numbers, hand):
    answer = ''
    keypad = [[1,2,3],[4,5,6],[7,8,9],[-1,0,-2]]
    L = -1
    R = -2
    
    for n in numbers:
        if n in [1,4,7]:
            answer += "L"
            L = n
        elif n in [3,6,9]:
            answer += "R"
            R = n
        else:
            n_coor = [(i, j) for i in range(4) for j in range(3) if keypad[i][j] == n][0]
            L_coor = [(i, j) for i in range(4) for j in range(3) if keypad[i][j] == L][0]
            R_coor = [(i, j) for i in range(4) for j in range(3) if keypad[i][j] == R][0]
            
            L_diff = abs(n_coor[0]-L_coor[0]) + abs(n_coor[1]-L_coor[1])
            R_diff = abs(n_coor[0]-R_coor[0]) + abs(n_coor[1]-R_coor[1])
            
            if (L_diff > R_diff) or (L_diff == R_diff and hand == 'right'):
                answer += "R"
                R = n
            elif (L_diff < R_diff) or (L_diff == R_diff and hand == 'left'):
                answer += "L"
                L = n
        
    return answer