import sys
sys.setrecursionlimit(10**9)
n, m, start = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 1

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, v, visited):
    global count
    visited[v] = count
    graph[v].sort()
    for i in graph[v]:
        if not visited[i]:
            count += 1
            dfs(graph, i, visited)


dfs(graph, start, visited)
for i in range(1, n + 1):
    print(visited[i])
