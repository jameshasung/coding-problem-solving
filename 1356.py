import sys

n = list(map(str, sys.stdin.readline().rstrip()))

for i in range(1, len(n)):
    first = 1
    for x in n[:i]:
        first *= int(x)
    end = 1 
    for x in n[i:]:
        end *= int(x)
    
    if first == end:
        print('YES')
        break

else: print('NO')
        
    
    

