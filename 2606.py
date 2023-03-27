import sys 

n = int(sys.stdin.readline())
pair = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
for i in range(pair):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

visited = [0] * (n+1)
def dfs(c):
    visited[c] = 1
    for n in graph[c]:
        if not visited[n]:
            dfs(n)
            
dfs(1)
print(visited.count(1) - 1)
