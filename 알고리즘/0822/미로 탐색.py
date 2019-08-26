def BFS(sy, sx):
    global r
    v[sy][sx] = 1
    D[sy][sx] = 1
    
    while Q:
        sy, sx = Q.pop(0)
        for i in range(4):
            ny = sy + dy[i]
            nx = sx + dx[i]
            if 0 <= ny < N and 0<= nx < M and m[ny][nx] == 1 and v[ny][nx] != 1:
                Q.append((ny, nx))
                v[ny][nx] = 1
                D[ny][nx] = D[sy][sx] + 1
                if ny == N-1 and nx == M-1:
                    r = D[ny][nx] 
                    return
  
N,M=list(map(int,input().split()))
m=[list(map(int,input())) for _ in range(N)]

dy = [1,-1,0,0]
dx = [0,0,1,-1]

r=0
Q=[(0,0)]
v=[[0]*M for i in range(N+1)]
D=[[0]*M for i in range(N+1)]
BFS(0,0)
print(r)

