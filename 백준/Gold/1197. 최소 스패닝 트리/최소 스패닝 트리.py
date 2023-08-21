def find_parent(x):
  if parent[x] != x:
    parent[x] = find_parent(parent[x])
  return parent[x]

def union(a, b):
  a = find_parent(a)
  b = find_parent(b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
  
V, E = map(int, input().split())
edges = []
parent = [i for i in range(V+1)]
MST = 0
for _ in range(E):
  A, B, C = map(int, input().split())
  edges.append((A,B,C))
edges = sorted(edges, key=lambda x:x[2])

for a, b, c in edges:
  if find_parent(a) != find_parent(b):
    union(a, b)
    MST += c

print(MST)