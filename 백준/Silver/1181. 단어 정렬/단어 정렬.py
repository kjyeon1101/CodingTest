N = int(input())
words = []

for _ in range(N):
  words.append(input())

words = sorted(list(set(words)), key=lambda x:(len(x), x))

for w in words:
  print(w)