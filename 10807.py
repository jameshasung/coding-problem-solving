import sys 

n = int(sys.stdin.readline())
ary = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())
print(ary.count(v))