import sys
sys.stdin = open("DFSinput.txt", "r")

V,E = map(int, input().split())      # 정점수, 간선수
G = [[] for _ in range(V+1)]         # 정점번호 1 ~ v
visit = [False for _ in range(V+1)]  # 방문정보

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)   # 무향 그래프

def DFS(v):
    S = []
    S.append(v)
    visit[v]=True



