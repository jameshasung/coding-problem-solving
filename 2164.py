import sys
from collections import deque
n = int(sys.stdin.readline())
ary = deque([i for i in range(1, n+1)])

while len(ary) != 1:
    ary.popleft()
    num = ary.popleft()
    ary.append(num)

print(ary[0])
