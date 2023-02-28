import sys
# 전체 케이스 T 입력
T = int(sys.stdin.readline())
for i in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    for j in range(n):
        count = 0
        cx, cy, r = map(int, sys.stdin.readline().split())
        # 점과 원의 거리를 구하는 공식
        # 행성 중심 ~ 출발점 까지의 거리
        d1 = ((x1 - cx)**2 + (y1 - cy)**2)**0.5
        # 행성 중심 ~ 도착점 까지의 거리
        d2 = ((x2 - cx)**2 + (y2 - cy)**2)**0.5

        if d1 < r and d2 < r:
            pass
        elif d1 < r:
            count += 1
        elif d2 < r:
            count += 1
    print(count)
