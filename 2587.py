import sys 

ary = []
for _ in range(5):
    ary.append(int(sys.stdin.readline()))

print(round(sum(ary)/5))
ary.sort()
print(ary[2])