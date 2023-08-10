import sys
input = sys.stdin.readline

def DaC(a, b, c):
  if b == 1:
    return a % c
  tmp = DaC(a, b//2, c)
  if b % 2 == 0:
    return (tmp * tmp) % c
  else:
    return (tmp * tmp * (a % c)) % c

A, B, C = map(int, input().split())
print(DaC(A, B, C))