numbers = []

while True:
  n = int(input())
  if n == 0:
    break
  numbers.append(n)

for n in numbers:
  r = list(str(n))
  r.reverse()
  r = int("".join(r))
  if n == r:
    print("yes")
  else:
    print("no")