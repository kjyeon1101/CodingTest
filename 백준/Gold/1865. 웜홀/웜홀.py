TC = int(input())
INF = 1e8
for _ in range(TC):
  N, M, W = map(int, input().split())
  edges = []
  for _ in range(M):
    S, E, T = map(int, input().split())
    edges.append((S,E,T))
    edges.append((E,S,T))
  for _ in range(W):
    S, E, T = map(int, input().split())
    edges.append((S,E,-T))

  distance = [INF for _ in range(N+1)]
  distance[1] = 0
  flag = 0
  
  for i in range(N):
    for s, e, t in edges:
      if distance[e] > distance[s] + t:
        distance[e] = distance[s] + t
        if i == N-1:
          flag = 1
          
  if flag == 1:
    print("YES")
  else:
    print("NO")