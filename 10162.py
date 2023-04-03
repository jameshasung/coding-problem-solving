import sys 

minutes = [300, 60, 10]
count = []

n = int(sys.stdin.readline())
for minute in minutes:
    cnt = 0
    if n // minute > 0:
        cnt += n//minute
        n %= minute
        count.append(cnt)
    else :
        count.append(cnt)
word = ''
if n % 10 > 0:
    print(-1)
else:    
    for i in count:
        print(i, end= ' ')
    print()
