# 왕실의 나이트

import sys

input_data = sys.stdin.readline().rstrip()
row = int(input_data[1])
col = input_data[0]

steps = [(2, 1,), (2, -1,), (-2, 1,), (-2, -1,),
         (1, 2,), (1, -2,), (-1, 2,), (-1, -2,)]
count = 0
for step in steps:
    next_row = row + step[0]
    next_col = ord(col) + step[1]

    if (next_row >= 1 and next_row <= 8) and (next_col >= ord('a') and next_col <= ord('h')):
        count += 1


print(count)
