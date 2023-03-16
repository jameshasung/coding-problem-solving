import sys


def binary_search(ary, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if ary[mid] == target:
            return mid
        elif ary[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(sys.stdin.readline().strip())
ary1 = sorted(list(map(int, sys.stdin.readline().strip().split())))

m = int(sys.stdin.readline().strip())
ary2 = list(map(int, sys.stdin.readline().strip().split()))

for i in ary2:
    result = binary_search(ary1, i, 0, n - 1)
    if result is None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
