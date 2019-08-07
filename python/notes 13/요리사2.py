N = int(input())
for i in range(N):
    m = [list(map(int,input().split())) for i in range(N)]    
    D = [i for i in range(N)]
    F = []   
    for i in range(1 << N):
        a = []
        for j in range(N):
            if i & (1 << j):
                a.append(D[j])
        if len(a) == 4:
            F.append(a)
    
    d = [0,1,2,3]
    f = []
    for i in range(1 << 4):
        b = []
        for j in range(4):
            if i & (1 << j):
                b.append(d[j])
        if len(b) == 2:
            f.append(b)
    
    r = []
    for i in range(len(f)-1):
        for j in range(i + 1, len(f)):
            if f[i][0] not in f[j] and f[i][1] not in f[j]:
                r.append(f[i]+f[j])
    
    R = []
    for k in r:        
        R.append(abs((m[k[0]][k[1]]+m[k[1]][k[0]])-(m[k[3]][k[2]]+m[k[2]][k[3]])))
    print(min(R))

                

            
   
    

        
                

    
    