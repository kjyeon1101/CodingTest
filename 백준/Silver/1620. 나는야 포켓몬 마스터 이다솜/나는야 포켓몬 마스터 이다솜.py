import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemons = dict()
for i in range(N):
  pokemons[i+1] = input().strip()
pokemons2 = dict(map(reversed, pokemons.items()))

for _ in range(M):
  q = input().strip()
  if q.isdigit():
    print(pokemons[int(q)])
  else:
    print(pokemons2[q])