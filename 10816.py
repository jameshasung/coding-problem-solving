import sys

count = {}
n = int(sys.stdin.readline().strip())
ary1 = sorted(list(map(int, sys.stdin.readline().strip().split())))
m = int(sys.stdin.readline().strip())
ary2 = list(map(int, sys.stdin.readline().strip().split()))

for i in ary1:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1


def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return count.get(target)
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


for i in ary2:
    print(binary_search(ary1, i, 0, n - 1), end=' ')
