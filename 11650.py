import sys

n = int(sys.stdin.readline().strip())

arr = []
for i in range(n):
    [x, y] = map(int, sys.stdin.readline().split())
    arr.append([x, y])

sort_arr = sorted(arr)

for i in sort_arr:
    print(i[0], i[1])
