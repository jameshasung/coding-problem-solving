import sys 

n = list(map(int, sys.stdin.readline().split()))
x = min(n)
while True:    
    cnt = 0
    for i in range(len(n)):
        if x % n[i] == 0:
            cnt += 1
    if cnt >= 3:
        print(x)
        break
    x += 1