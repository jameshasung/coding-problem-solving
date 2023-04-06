import sys 

a, b = list(map(int, sys.stdin.readline().split()))
ary = [] 
sum_n = 0
for i in range(b-1):
    for _ in range(i):
        ary.append(i)
    if len(ary) >= b:
        break
for i in range(a - 1, b):
    sum_n += ary[i]
print(sum_n)