import sys
input = sys.stdin.readline

white = 0
blue = 0

def divide_paper(paper):
  global white
  global blue

  cnt = 0
  size = len(paper) * len(paper)
  for p in paper:
    cnt += p.count(0) # 하얀색 개수
    
  if cnt == size: # 모두 하얀색
    white += 1
    return
  elif cnt == 0: # 모두 파란색
    blue += 1
    return

  # 모두 같은색 X
  N = len(paper)
  I = []
  II = []
  III = []
  IV = []
  for p in paper[:N//2]:
    I.append(p[:N//2])
    II.append(p[N//2:])
  for p in paper[N//2:]:
    III.append(p[:N//2])
    IV.append(p[N//2:])
    
  divide_paper(I)
  divide_paper(II)
  divide_paper(III)
  divide_paper(IV)
  

def main():
  global white
  global blue
  N = int(input())
  paper = []
  for _ in range(N):
    row = list(map(int, input().split()))
    paper.append(row)
  divide_paper(paper)
  print(white)
  print(blue)

main()