import sys 
t = int(sys.stdin.readline())

for i in range(t):
    ary = list(map(int, sys.stdin.readline().split()))
    
    ary.sort()
    ary.pop(-1)
    ary.pop(0)
    
    max_n = max(ary)
    min_n = min(ary)
    sum_n = sum(ary)
    if max_n - min_n >= 4:
        print('KIN')
    else: 
        print(sum_n)
        