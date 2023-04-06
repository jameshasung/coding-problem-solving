import sys

s = sys.stdin.readline().rstrip()
p = sys.stdin.readline().rstrip()

if s.count(p) > 0:
    print(1)
else:
    print(0)