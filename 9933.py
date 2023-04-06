import sys 

n = int(sys.stdin.readline())
ary = []
for _ in range(n):
    ary.append(sys.stdin.readline().rstrip())

for i in range(n):
    if ary.count(ary[i]) > 0 and ary.count(ary[i][::-1]) > 0:
        size = len(ary[i])
        print(size, ary[i][size//2])
        break
        
    
    