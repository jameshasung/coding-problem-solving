# 합이 S인 K개의 양의 정수
import sys

s, k = map(int, sys.stdin.readline().strip().split())

# a = 몫
a = s // k
# b = 나머지
b = s % k
n = 1

for i in range(k):
    if b > 0:
        n *= a + 1
        b -= 1
    else:
        n *= a

print(n)
