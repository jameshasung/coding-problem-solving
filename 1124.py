# 자연수 X를 소인수분해하면, 곱해서 X가 되는 소수의 목록을 얻을 수 있다.
# 예를 들어, 12 = 2 × 2 × 3이다. 1은 소수가 아니다.
# 어떤 수 X를 소인수분해 해서 구한 소수의 목록의 길이가 소수이면, 그 수를 언더프라임 이라고 한다.
# 12는 목록에 포함된 소수의 개수가 3개이고, 3은 소수이니 12는 언더프라임이다.
# 두 정수 A와 B가 주어졌을 때, A보다 크거나 같고, B보다 작거나 같은 정수 중에서 언더프라임인 것의 개수를 구해보자.
import sys

# 입력 받기
A, B = map(int, sys.stdin.readline().split())

# 소인수 분해를 수행하는 함수 정의


def factorize(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    return factors


# A부터 B까지의 언더프라임 개수를 구하기
count = 0
for n in range(A, B+1):
    if len(factorize(n)) == 0:
        continue
    if len(factorize(len(factorize(n)))) == 1:
        count += 1

# 결과 출력하기
print(count)
