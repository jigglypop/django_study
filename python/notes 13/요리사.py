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
        if len(a) == 2:
            F.append(a)
       
    r = []
    for i in range(len(F)-1):
        for j in range(i + 1, len(F)):
            if F[i][0] not in F[j] and F[i][1] not in F[j]:
                r.append(F[i]+F[j])
   
    R = []
    for k in r:        
        R.append(abs((m[k[0]][k[1]]+m[k[1]][k[0]])-(m[k[3]][k[2]]+m[k[2]][k[3]])))
    print(min(R))
    

    
        
  
