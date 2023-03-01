import sys

X = int(sys.stdin.readline().rstrip())
stick = 64

if X == 64:
    print(1)
else:
    count = 0
    while X > 0:
        if X >= stick:
            X -= stick
            count += 1
        else:
            stick //= 2
    print(count)
