import sys
import math

T = int(sys.stdin.readline())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,  sys.stdin.readline().split())
    # 원의 방정식
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if d == 0 and r1 == r2:
        print(-1)
    elif abs(r2 - r1) == d or (r1+r2) == d:
        print(1)
    elif abs(r2 - r1) < d < (r1+r2):
        print(2)
    else:
        print(0)
