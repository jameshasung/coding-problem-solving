import sys


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


T = int(sys.stdin.readline())
for i in range(T):
    n, m = map(int, sys.stdin.readline().split())
    print(factorial(m) // (factorial(n) * factorial(m-n)))
