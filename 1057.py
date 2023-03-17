import sys

n, jm, hs = map(int, sys.stdin.readline().split())
count = 0
while jm != hs:
    jm -= jm // 2
    hs -= hs // 2
    count += 1
print(count)
