import sys

n, m = map(int, sys.stdin.readline().strip().split())
ary = list(map(int, sys.stdin.readline().strip().split()))


def binary_search(ary, target):
    start = 0
    end = max(ary)
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for i in ary:
            if i > mid:
                total += i - mid
        # 떡이 부족한 경우 더 많이 자르기
        if total < target:
            end = mid - 1
        # 떡이 충분한 경우 덜 자르기
        else:
            result = mid
            start = mid + 1
    return result


print(binary_search(ary, m))
