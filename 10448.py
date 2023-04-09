import sys 
n = int(sys.stdin.readline())
x = 1
T = []
sum_n = [0]*1001
    
while x < 100:
    T.append(x*(x+1)//2)
    x +=1

for i in range(len(T)):
    for j in range(len(T)):
        for k in range(len(T)):
            num = T[i]+T[j]+T[k]
            if num <= 1000:
                sum_n[num] = 1
for _ in range(n):
    print(sum_n[int(input())])
            
            
            