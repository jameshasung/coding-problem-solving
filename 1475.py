import sys 
import math

n = sys.stdin.readline()
ary = []
for i in range(0, 10):
    ary.append(n.count(str(i)))
ary[6] += ary[9]
ary.pop()

if max(ary) == ary[6]:
    if ary[6] % 2 == 0:
        ary[6] //= 2
    else :
        ary[6] = ary[6] // 2 + 1

print(max(ary))