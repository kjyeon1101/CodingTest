def solution(arr):
    num = len(arr)//2+1
    dp_max = [[-10000 if i!=j else int(arr[i*2]) for i in range(num)] for j in range(num)]
    dp_min = [[10000 if i!=j else int(arr[i*2]) for i in range(num)] for j in range(num)]
    
    for calc in range(1, num):
        for i in range(num - calc):
            j = calc + i
            for k in range(i,j):
                if arr[2*k+1] == "+":
                    dp_max[i][j] = max(dp_max[i][k] + dp_max[k + 1][j], dp_max[i][j])
                    dp_min[i][j] = min(dp_min[i][k] + dp_min[k + 1][j], dp_min[i][j])
                else:
                    dp_max[i][j] = max(dp_max[i][k] - dp_min[k + 1][j], dp_max[i][j])
                    dp_min[i][j] = min(dp_min[i][k] - dp_max[k + 1][j], dp_min[i][j])
    
    answer = dp_max[0][num-1]
    return answer