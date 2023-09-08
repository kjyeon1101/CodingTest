import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
a = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
if a == 0:
    if (y1-y3)*(x1-x2) != (y1-y2)*(x1-x3): # 평행
        print(0)
    else: # 일치
        xl = min(max(x1,x2), max(x3,x4))
        xr = max(min(x1,x2), min(x3,x4))
        yl = min(max(y1,y2), max(y3,y4))
        yr = max(min(y1,y2), min(y3,y4))
        if xl < xr or yl < yr:
            print(0)
        else:
            print(1)
else:
    Px = (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4)
    Py = (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4)
    Px /= a
    Py /= a
    if Px < min(x1,x2) or Px > max(x1,x2) or Px < min(x3,x4) or Px > max(x3,x4):
        print(0)
    elif Py < min(y1,y2) or Py > max(y1,y2) or Py < min(y3,y4) or Py > max(y3,y4):
        print(0)
    else:
        print(1)