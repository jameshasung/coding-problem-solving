import sys 

arr = ['E','A','B','C','D']

s = []
for i in range(3):
    
    s.append(input())
for i in range(len(s)):    
    print(arr[s[i].count('0')])