import sys

n, k = map(int, sys.stdin.readline().split())
coin_list = []
for i in range(n):
    coin_list.append(int(sys.stdin.readline()))

coin_list.sort(reverse=True)
count = 0

for coin in coin_list:
    coin_num = k // coin
    count += coin_num
    k -= coin_num * coin
    if k == 0:
        break

print(count)
