import sys 

word = sys.stdin.readline().rstrip()
find = sys.stdin.readline().rstrip()
cnt = 0 
cnt = word.count(find)
print(cnt)