import sys 

t = int(sys.stdin.readline())

def sol(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return sol(n-3) + sol(n-2) + sol(n-1)

for _ in range(t):
    print(sol(int(sys.stdin.readline())))


    