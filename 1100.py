import sys

chess = []
count = 0
n = 8
for _ in range(n):
    str = sys.stdin.readline().strip()
    chess.append(str)

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:  # 하얀칸일 경우
            if chess[i][j] == 'F':  # F있을 경우
                count += 1
print(count)
