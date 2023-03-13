import sys

k = int(sys.stdin.readline().strip())
ary = []
for i in range(k):
    n = int(sys.stdin.readline().strip())
    ary.append(n)
    if (n == 0):
        ary.pop()
        ary.pop()
print(sum(ary))
