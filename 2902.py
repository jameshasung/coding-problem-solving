import sys 

str = list(map(str, sys.stdin.readline().split('-')))
answer = ''
for i in range(len(str)):
    answer += str[i][0]

print(answer)
    