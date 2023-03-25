import sys

n = int(sys.stdin.readline())
paper = [[0] * 100 for _ in range(100)]  # 100 x 100 paper
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1
result = 0

for i in range(100):
    result += sum(paper[i])

print(result)
