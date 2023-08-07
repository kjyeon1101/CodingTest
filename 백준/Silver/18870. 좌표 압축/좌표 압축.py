import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
sortedX = sorted(list(set(X)))
sortedX_dict = dict()

for i, x in enumerate(sortedX):
  sortedX_dict[x] = i

answer = " ".join([str(sortedX_dict[x]) for x in X])
print(answer.strip())