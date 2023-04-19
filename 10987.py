import sys 
word = sys.stdin.readline().rstrip()
ary = ['a','e','i','o','u']
answer = 0

for i in range(len(word)):
    for j in range(len(ary)):
        if word[i] == ary[j]:
            answer += 1
    
    
print(answer)