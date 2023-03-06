import sys

n, m = map(int, sys.stdin.readline().split())
no_see = set()
no_hear = set()
no_see_hear = set()

for i in range(n):
    no_see.add(sys.stdin.readline().strip())
for i in range(m):
    no_hear.add(sys.stdin.readline().strip())

no_see_hear = sorted(no_see.intersection(no_hear))
print(len(no_see_hear))
for i in no_see_hear:
    print(i)
