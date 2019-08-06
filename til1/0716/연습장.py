def DFS(sy, sx):

    global r 

    if M[sy][sx]  == 3:
        r = 1
        return
    
    Q.append((sy, sx))
    for i in range(4):
        ny = sy + dy[i]
        nx = sx + dx[i]
        if 0 <= ny < N 
            and 0 <= nx < N
            and M[ny][nx] != 1
            and (ny, nx) not in Q:

            DFS(ny, nx)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input())) for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if M[y][x] == 2:
                sy, sx = y, x

    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    Q = []
    r = 0
    DFS(sy, sx)
    print(f'#{tc} {r}')