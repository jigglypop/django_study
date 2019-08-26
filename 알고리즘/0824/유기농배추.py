import sys
sys.setrecursionlimit(10000)

def DFS(sy,sx):
    m[sy][sx] = 0
    dy = [-1,1,0,0]
    dx = [0,0,1,-1]
    for i in range(4):      
        ny = sy + dy[i]
        nx = sx + dx[i]
        if m[ny][nx] == 1:
            DFS(ny,nx)
       
T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    m = [[0]*(M+2) for _ in range(N+2)]
    for _ in range(K):
        i,j = map(int,input().split())
        I = i+1
        J = j+1
        m[J][I] = 1
        
    c = 0
    for y in range(N+2):
        for x in range(M+2):
            if m[y][x] == 1:
                c += 1
                DFS(y,x)
    print(c)   
    