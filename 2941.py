import sys

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = sys.stdin.readline().strip()

for i in croatia:
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(word.__len__())
