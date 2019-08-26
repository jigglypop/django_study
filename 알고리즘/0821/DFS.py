def DFS(v):
    S = []
    S.append(v)     # S = [1]
    visit[v] = True
    while S:
        for w in G[v]:         
            if not visit[w]:
                S.append(w)
                v = w
                visit[w] = True
                break
        else:
            v = S.pop()
# ----------------------------------------------
import sys

sys.stdin = open("DFSinput.txt", "r")
V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
visit = [False for _ in range(V + 1)]

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

print(G)
DFS(1)