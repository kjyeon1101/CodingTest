def check(a, b, n, m, maps, routes, idx):
    if a < 0 or a >= n:
        return 0
    if b < 0 or b >= m:
        return 0
    if maps[a][b] == 0:
        return 0
    if (a,b) in routes[idx-1]:
        return 0
    if len(routes) > idx + 1:
        if (a,b) in routes[idx+1]:
            return 0
    return 1

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    routes = [[(0,0)]]
    idx = 0
    
    while True:
        if len(routes) <= idx:
            answer = -1
            break
            
        route = routes[idx]

        for r in route:
            left = (r[0], r[1]-1)
            right = (r[0], r[1]+1)
            up = (r[0]-1, r[1])
            down = (r[0]+1, r[1])
            
            if check(left[0], left[1], n, m, maps, routes, idx):
                if len(routes) == idx + 1:
                    routes.append([left])
                else:
                    routes[idx+1] += [left]
                    
            if check(right[0], right[1], n, m, maps, routes, idx):
                if len(routes) == idx + 1:
                    routes.append([right])
                else:
                    routes[idx+1] += [right]
                    
            if check(up[0], up[1], n, m, maps, routes, idx):
                if len(routes) == idx + 1:
                    routes.append([up])
                else:
                    routes[idx+1] += [up]
            
            if check(down[0], down[1], n, m, maps, routes, idx):
                if len(routes) == idx + 1:
                    routes.append([down])
                else:
                    routes[idx+1] += [down]
        
        if len(routes) > idx + 1:
            if (n-1, m-1) in routes[idx+1]:
                answer = idx + 2
                break
        else:
            if (n-1, m-1) in route:
                answer = idx + 1
                break
            
        idx += 1

    return answer