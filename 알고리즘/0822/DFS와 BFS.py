import sys
from collections import deque


def DFS(s):
    visitd[s] = True
    global r2
    r2.append(s)
    for w in sorted(G[s]):
        if not visitd[w]:
            visitd[w] = True            
            DFS(w)
def BFS(s):
    Q = deque([s])
    r = []
    visitb[s] = True
    while Q:
        v = Q.popleft()
        r.append(v)
        for w in sorted(G[v]):
            if not visitb[w]:
                Q.append(w)
                visitb[w] = True
    return ' '.join(map(str,r))

# sys.stdin = open('input.txt','r')
V,E,s = map(int,sys.stdin.readline().split())

G = [[] for _ in range(V+1)]
visitb = [False for _ in range(V+1)]
visitd = [False for _ in range(V+1)]
for _ in range(E):
    u, v = map(int,sys.stdin.readline().split())
    G[u].append(v)
    G[v].append(u)

r2 = []
DFS(s)
print(' '.join(map(str,r2)))
print(BFS(s))
