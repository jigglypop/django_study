def DFS(v):   
    visit[v] = True   
    for w in G[v]:        
        if not visit[w]:
            DFS(w)        
import sys

sys.stdin = open("input (17).txt", "r")
for _ in range(10):
    tc, N = list(map(int,input().split()))
    m = list(map(int,input().split()))
    M = [[0,0] for _ in range(N)]

    for i in range(N):
        M[i][0] = m[i*2]
        M[i][1] = m[i*2+1] 

    G = [[] for _ in range(100)]
    visit = [False for _ in range(100)]

    for i in M:
        G[i[0]].append(i[1])
        #G[i[1]].append(i[0])

    DFS(0)
    print(f'#{tc} {int(visit[99])}')