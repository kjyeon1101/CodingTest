import sys
input = sys.stdin.readline

def DaC(n, A):
  if n == 1:
    return A
  tmp = DaC(n//2, A)
  if n % 2 == 0:
    return matrix_multiple(tmp, tmp)
  else:
    return matrix_multiple(matrix_multiple(tmp, tmp), A)

def matrix_multiple(A, B):
  result = []
  for i in range(2):
    tmp = []
    for j in range(2):
      s = 0
      for k in range(2):
        s += A[i][k] * B[k][j]
      tmp.append(s%1000000007)
    result.append(tmp)
  return result
      
n = int(input())
A = [[1,1],[1,0]]
print(DaC(n, A)[0][1]%1000000007)