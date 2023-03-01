import sys

word = sys.stdin.readline().rstrip()
word = word.upper()
unique_word = list(set(word))
count_list = []

for i in unique_word:
    count = word.count(i)
    count_list.append(count)

if count_list.count(max(count_list)) > 1:
    print("?")
else:
    print(unique_word[(count_list.index(max(count_list)))])
