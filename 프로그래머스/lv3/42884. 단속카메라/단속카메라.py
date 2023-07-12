def solution(routes):
    answer = 1
    routes = sorted(routes, key=lambda x:x[0])
    camera = routes[0]
    
    for route in routes[1:]:
        if camera[0] <= route[0] <= camera[1]:
            camera = [max(camera[0], route[0]), min(camera[1], route[1])]
        else:
            camera = route
            answer += 1
        
    return answer