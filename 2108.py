# 5
# 1
# 3
# 8
# -2
# 2
import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline()))    
    
# 데이터 정렬
data.sort()

# 평균구하기 
mean = round(sum(data)/n)
print(mean)

# 중앙값 구하기
middle = data[n//2]
print(middle)

# 최빈값 구하기
for i in range(n):
    data[i] = data[i]+4000
    
count = [0]*8001
for i in range(n):
    count[data[i]] += 1
    
max_count = max(count)
max_index = count.index(max_count)
count[max_index] = 0
if max_count == max(count):
    max_index = count.index(max_count)

print(max_index-4000)

# 범위 구하기
print(data[-1]-data[0])