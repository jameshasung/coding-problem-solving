import sys 

n = int(sys.stdin.readline())
ary = []
cnt = []
for i in range(n):
    ary.append(sys.stdin.readline().rstrip())
ary.sort()
for i in range(len(ary)):
    cnt.append(ary.count(ary[i]))
print(ary[cnt.index(max(cnt))])

        
    