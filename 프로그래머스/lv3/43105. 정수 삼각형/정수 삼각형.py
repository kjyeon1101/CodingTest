def solution(triangle):
    top = triangle[0][0]
    triangle.reverse()
    route_sum = triangle[0]
    
    for tri in triangle[1:len(triangle)-1]:
        new_sum = []
        for i, t in enumerate(tri):
            new_sum.append(t + max(route_sum[i], route_sum[i+1]))
        route_sum = new_sum
    
    answer = max(route_sum) + top
    return answer