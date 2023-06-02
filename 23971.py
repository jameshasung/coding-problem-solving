import sys
import math
h, w, n, m = map(int, sys.stdin.readline().split())


a = math.ceil(h/(n+1)) # 세로에 몇 명이 앉는지를 계산합니다
b = math.ceil(w/(m+1)) # 가로에 몇 명이 앉는지를 계산합니다
answer = a*b #가로와 세로의 값을 곱합니다
print(answer)