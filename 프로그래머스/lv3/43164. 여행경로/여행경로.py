answer = []
goal = 0

def dfs(tickets, used, path):
    global answer
    global goal
    now = path[-1]
    
    if len(path) == goal:
        answer.append(path)
        return
    
    for i, ticket in enumerate(tickets):
        if ticket[0] == now and used[i] == False:
            used[i] = True
            dfs(tickets, used, path+[ticket[1]])
            used[i] = False

def solution(tickets):
    global answer
    global goal
    
    goal = len(tickets) + 1
    used = [False] * len(tickets)
    path = ["ICN"]
    dfs(tickets, used, path)
    answer.sort()
    
    return answer[0]