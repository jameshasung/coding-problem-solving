import sys 
from collections import deque

#  정점의 개수 N(1 ≤ N ≤ 1,000), 
#  간선의 개수 M(1 ≤ M ≤ 10,000), 
#  탐색을 시작할 정점의 번호 V

n, m, v = map(int, sys.stdin.readline().split())


visited_dfs = [0] *(n+1)
ans_dfs = []
visited_bfs = [0] *(n+1)
ans_bfs = []

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    # 양방향 
    
# 정점 번호가 작은 것을 먼저 방문
for i in range(1, n+1):
    graph[i].sort()
    
def dfs(c):
    ans_dfs.append(c)
    visited_dfs[c] = 1 # 방문했다고 표시
    for n in graph[c]:
        if not visited_dfs[n]:
            dfs(n)

def bfs(c):
    q = deque([c])
    q.append(c)
    ans_bfs.append(c)
    visited_bfs[c] = 1
    while q: 
        data = q.popleft()
        for n in graph[data]:
            if not visited_bfs[n]: # 방문하지 않았다면 q 에 삽입
                q.append(n)
                ans_bfs.append(n)
                visited_bfs[n] = 1
                
dfs(v)
bfs(v)
print(*ans_dfs)
print(*ans_bfs)
    
    