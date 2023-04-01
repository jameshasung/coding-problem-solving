# 요세푸스 문제는 다음과 같다.

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
# 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
# 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
# 12(3)4567 # 3
# 45(6)712 # 6
# 71(2)45 # 2
# 45(7)1 # 7
# 14(5) # 5
# # 1
# # 4
import sys 
from collections import deque

queue = deque()
n, k = map(int, sys.stdin.readline().split())
answer = []
for i in range(1, n + 1):
    queue.append(i)

while queue:
    for i in range(k - 1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())
    
print('<', end = '')
print(', '.join(map(str, answer)), end = '')
print('>')