from collections import deque
import sys


def BFS(s):
    Q = deque()
    D[s] = 0
    visit[s] = True
    Q.append(s)
    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visit[w]:
                visit[w] = True 
                D[w] = D[v] + 1
                P[w] = v
                print(w)
                Q.append(w)           
                

import sys
sys.stdin = open("DFSinput.txt", "r")

V,E = map(int, input().split())      # 정점수, 간선수
G = [[] for _ in range(V+1)]         # 정점번호 1 ~ v
visit = [False for _ in range(V+1)]  # 방문정보
D = [0 for _ in range(V+1)] 
P = [0 for _ in range(V+1)] 
for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)   # 무향 그래프

for i in range(1, V+1):
    print(i, '-->', G[i])
BFS(1)
print(D)
print(P)


