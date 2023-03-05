import sys
import collections

word = sys.stdin.readline().rstrip()
check_word = collections.Counter(word)
cnt = 0
mid = ''
answer = ''
# print(check_word)
for i, j in check_word.items():
    if j % 2 == 1:
        cnt += 1
        mid = i  # 중간에 들어가는 문자
        if cnt >= 2:
            print("I'm Sorry Hansoo")
            exit()
for i, j in sorted(check_word.items()):
    answer += i * (j // 2)  # 절반으로 나뉜 문자열을 만들어야 하므로 현재 갯수를 2로 나눠줌
print(answer + mid + answer[::-1])
