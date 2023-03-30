n = input()
length = len(n) - 1
result = 0
for i in range(length):
    result += (9 * (10 ** i)) * (i + 1) # i+1번째 자릿수의 숫자 개수 * 길이
result += ((int(n) - (10 ** length)) + 1) * (length + 1) # 가장 높은 자릿수의 숫자 개수 * 길이
print(result)