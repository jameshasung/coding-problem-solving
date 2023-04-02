import sys 

n, m  = map(int, sys.stdin.readline().split())
result = []
count = 0 
for i in range(n):
    person, limit = map(int, sys.stdin.readline().split())
    mile = list((map(int, sys.stdin.readline().split())))
    mile.sort(reverse=True)
    if(person < limit):
        result.append(1)
    else: 
        result.append(mile[limit - 1])
result.sort()

for i in result:
    m -= i
    
    if m < 0 : 
        break
    else :
        count += 1        
print(count)
