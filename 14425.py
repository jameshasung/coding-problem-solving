import sys

n, m = map(int, sys.stdin.readline().strip().split())
s = set()
s2 = set()
count = 0
for i in range(n):
    word = sys.stdin.readline().strip()
    s.add(word)
for i in range(m):
    word = sys.stdin.readline().strip()
    if word in s:
        count += 1
print(count)
