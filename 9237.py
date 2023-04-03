import sys
# 4
# 2 3 4 3
# 내림차순으로 정렬
# 제일 큰 거 심어 total = 1, total += max(ary)
# if(total > ary[0]):
#   continue
# if(total <)
n = int(sys.stdin.readline())
t = list(map(int, sys.stdin.readline().split()))
t.sort(reverse= True)

max_day = t[0]
if n == 1:
    print(n + 2)
else: 
    for i in range(1, n):
        if max_day < (i + t[i]):
            max_day = i + t[i]
    print(max_day + 2)

