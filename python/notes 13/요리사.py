T = int(input())
for tc in range(1,T+1):
    N = int(input())   
    m = [list(map(int,input().split())) for i in range(N)]    
    D = [i for i in range(N)]
    r = [[0]*N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if x < y:
                r[y][x] = m[y][x] + m[x][y]


    dy = []   
    for i in range(1 << N):
        a = []
        for j in range(N):
            if i & (1 << j):
                a.append(D[j])
        if len(a) == N/2:
            dy.append(a)


    dx = []
    for i in dy:
        d = set([i for i in range(N)])
        dx.append(list(d-set(i)))
    
    sdy = []
    for i in dy:
        s = 0
        for y in i:
            for x in i:
                s += r[y][x]
        sdy.append(s)
    

    sdx = []
    for i in dx:
        s = 0
        for y in i:
            for x in i:
                s += r[y][x]
        sdx.append(s)

    f = []
    for i in range(len(sdx)):
        f.append(abs(sdx[i]-sdy[i]))
    print(f'#{tc} {min(f)}')
                

            
   
    

        
                

    
    