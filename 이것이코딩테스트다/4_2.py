# 예제 4-2 시각
# 풀이시간 15분

import sys
n = int(sys.stdin.readline())
count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i):
                count += 1
            elif '3' in str(j):
                count += 1
            elif '3' in str(k):
                count += 1
print(count)
