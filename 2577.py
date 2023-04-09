import sys 

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

word = str(a*b*c)
for i in range(10):
    print(word.count(str(i)))