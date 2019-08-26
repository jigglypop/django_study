import sys
sys.setrecursionlimit(10000)

def DFS(v):
    visit[v] = True
    for w in G[v]:
        if visit[w] is False:
            DFS(w)

n, m = map(int, sys.stdin.readline().split())
G = [[] for _ in range(n+1)]
visit = [False]*(n+1)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    G[u].append(v)
    G[v].append(u)

c = 0
for i in range(1, n+1):
    if visit[i] is False:
        DFS(i)
        c += 1
print(c)

