from collections import Counter
t = int(input())

for i in range(t):
    n = int(input())
    wear = []
    for j in range(n):
        a, b = input().split()
        wear.append(b)

    wear_Counter = Counter(wear)
    cnt = 1 # 각 종류마다 항목의 개수

    for key in wear_Counter:
        cnt *= wear_Counter[key] + 1

    print(cnt-1)
    
    # 파이썬의 Counter모듈을 이용하여 딕셔너리를 직접 제작하지 않아도 자동으로 개수를 세주는 기능을 이용