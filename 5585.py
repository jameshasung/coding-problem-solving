import sys

n = 1000 - int(sys.stdin.readline())
coin_types = [500, 100, 50, 10, 5, 1]
count = 0
for coin in coin_types:
    count += n // coin
    n = n % coin
print(count)
