# 예제 4-1 상하좌우
# 제한시간 15분
# 풀이시간 약 3분
import sys

n = int(sys.stdin.readline())
map = [[0] * n for _ in range(n)]

cmd = list(sys.stdin.readline().split())

x, y = 1, 1
for i in range(len(cmd)):
    if (x == 1 and cmd[i] == 'L'):
        continue
    elif (y == 1 and cmd[i] == 'U'):
        continue
    elif (cmd[i] == 'R'):
        x += 1
    elif (cmd[i] == 'L'):
        x -= 1
    elif (cmd[i] == 'U'):
        y -= 1
    elif (cmd[i] == 'D'):
        y += 1

print(x, y)
