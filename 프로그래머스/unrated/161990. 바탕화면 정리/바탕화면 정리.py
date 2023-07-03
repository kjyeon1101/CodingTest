def solution(wallpaper):
    files = []
    for i, wall in enumerate(wallpaper):
        for j, w in enumerate(wall):
            if w == '#':
                files.append((i,j))

    min1 = min([f[0] for f in files])
    min2 = min([f[1] for f in files])
    
    max1 = max([f[0] for f in files]) + 1
    max2 = max([f[1] for f in files]) + 1
    
    answer = [min1, min2, max1, max2]
    
    return answer