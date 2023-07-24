numbers = []

while True:
  a, b, c = map(int, input().split())
  if a == 0 and b == 0 and c == 0:
    break
  numbers.append(sorted([a,b,c]))

for a, b, c in numbers:
  if a**2 + b**2 == c**2:
    print("right")
  else:
    print("wrong")