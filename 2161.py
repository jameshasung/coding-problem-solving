import sys
from collections import deque

trash = []
answer = []

def solution(ary):
    trash.append(ary[0])
    ary.popleft()
    ary.append(ary[0])
    ary.popleft()
        
n = int(sys.stdin.readline())
cards = deque()
for i in range(1,n+1):
    cards.append(i)
while len(cards) != 1:
    solution(cards)
for i in trash:
    answer.append(i)
answer.append(cards[0])
for i in answer:
    print(i, end=" ")
