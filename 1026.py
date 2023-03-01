import sys

N = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

s = 0
for i in range(N):
    s += min(a) * max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))

print(s)
