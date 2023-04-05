import sys 
from collections import deque
x, y = list(map(str, sys.stdin.readline().split()))

def rev(x):
    str = list(''.join(reversed(x)))
    while True:
            if str[0] == '0':
                str.pop(0)
            else: 
                break
    word = ''
    for i in range(len(str)):
        word += str[i]
    return word


print(rev(str(int(rev(x)) + int(rev(y)))))
        
    