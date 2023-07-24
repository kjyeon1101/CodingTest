from math import factorial

N, K = map(int, input().split())
answer = int(factorial(N) / (factorial(K) * factorial(N-K)))
print(answer)