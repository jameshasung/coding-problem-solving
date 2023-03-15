import sys

n = int(sys.stdin.readline().strip())
ary1 = set(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
ary2 = list(map(int, sys.stdin.readline().strip().split()))

for i in ary2:
    if i in ary1:
        print(1)
    else:
        print(0)
