import sys

k, n = map(int, sys.stdin.readline().strip().split())
ary = []
for i in range(k):
    ary.append(int(sys.stdin.readline().strip()))


def solution(ary, n):
    start = 1
    end = max(ary)
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for i in ary:
            count += i // mid
        if count >= n:
            start = mid + 1
        else:
            end = mid - 1
    return end


print(solution(ary, n))
