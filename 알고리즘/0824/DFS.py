import sys

sys.stdin = open('input.txt','r')
V,E = map(int,input().split())
G = [[] for _ in range(E)]
visit = [False for _ in range(V+1)]

for _ in range(E):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

# 양방향 그래프
print(G)
def DFS(s):
    print(s)
    visit[s] = True    
    for w in G[s]:
        if not visit[w]:      
            DFS(w)

print(DFS(1))

