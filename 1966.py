import sys
from collections import deque

case = int(sys.stdin.readline())

for i in range(case):
    n, m = list(map(int, sys.stdin.readline().split()))
    important = deque(list(map(int, sys.stdin.readline().split())))

    order = 0
    while important:
        best = max(important)
        first = important.popleft()
        m -= 1
        
        if best == first:
            order += 1
            if m < 0:
                print(order)
                break
            
        else:
            important.append(first)
            if m < 0:
                m = len(important) - 1
    
    