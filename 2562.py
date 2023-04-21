import sys 
ary =[]
for _ in range(9):
    ary.append(int(sys.stdin.readline()))

print(max(ary))
print(ary.index(max(ary)) + 1)
    