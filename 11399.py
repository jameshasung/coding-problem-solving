import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

p.sort()
answer = 0
for i in range(1, n+1):
    answer += sum(p[:i])
    # sum(p[:i]) is the same as sum(p[0:i])

print(answer)
