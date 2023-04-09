import sys

ary = []
sum_n = 0
for i in range(9):
    n = int(sys.stdin.readline())    
    ary.append(n)
    
sum_n = sum(ary)

to_remove = []
finish = False
for i in range(len(ary)):
    for j in range(i + 1, len(ary)):
        if ary[i] + ary[j] == sum_n - 100:
            to_remove.append(ary[i])
            to_remove.append(ary[j])
            finish = True
            break
    if finish:
        break

for n in to_remove:
    ary.remove(n)
ary.sort()
for n in ary:
    print(n)

