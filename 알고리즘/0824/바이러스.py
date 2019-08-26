import sys
import pprint

def DFS(v):
    global c
    visit[v] = True
    for w in G[v]:
        if not visit[w]: 
            c += 1         
            DFS(w)

# sys.stdin = open('input4.txt','r')
T = int(input())
n = int(input())
G = [[] for i in range(T+1)]
visit = [False for _ in range(T+1)]
for _ in range(n):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

c = 0
DFS(1)
print(c)

    


