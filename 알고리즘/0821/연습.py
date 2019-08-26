from collections import deque
import sys

def BFS(s):                                # s : 시작점
    # 시작점을 방문하고, 큐에 삽입
    Q = deque()
    r = []
    visit[s] = True
    Q.append(s)
    r.append(s)    
    while Q:
        v = Q.popleft()
        for w in sorted(G[v]):
            if not visit[w]:
                visit[w] = True
                Q.append(w)
                r.append(w)
    return ' '.join(map(str,r))
    # 큐를 생성. 빈 큐가 아닐 동안 
    # v : 큐에 정점을 하나 꺼내온다.
    # v의 방문하지 않은 인접 정점 w를 찾는다.
    # w를 방문하고 큐에 삽입


sys.stdin = open("DFSinput.txt", "r")

V,E,s = map(int, input().split())      # 정점수, 간선수
G = [[] for _ in range(V+1)]         # 정점번호 1 ~ v
visit = [False for _ in range(V+1)]  # 방문정보

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)   # 무향 그래프

print(BFS(s))
