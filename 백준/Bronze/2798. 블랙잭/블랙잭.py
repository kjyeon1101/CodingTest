from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))
card_sum = sorted(list(set([sum(i) for i in combinations(cards, 3)])))
answer = 0

for cs in card_sum:
  if cs <= M and cs > answer:
    answer = cs

print(answer)