import sys


def hansu(n):
    count = 0
    for i in range(1, n + 1):
        # 1 ~ 99 까지는 모두 등차수열이다. -> 한수임
        if i < 100:
            count += 1
        else:
            num = list(map(int, str(i)))
            # 각 자리수가 등차수열을 이루는지 확인
            if num[0] - num[1] == num[1] - num[2]:
                count += 1
    return count


n = int(sys.stdin.readline())
print(hansu(n))
