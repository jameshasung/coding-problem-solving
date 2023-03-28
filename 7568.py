import sys 

n = int(sys.stdin.readline())
ary = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    ary.append((x, y))

for i in ary:
    rank = 1
    for j in ary:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')