def perm(k,n,used):
    if k == n:             
        for i in range(n):
            print(arr[order[i]],end = ' ')
        print()
        return 
    
    for i in range(n):
        if used & (1 << i): continue
        order[k] = i
        print(bin(used))
        perm(k+1, n, used|(1<<i))

N,M = map(int,input().split())
arr = [i for i in range(1,N+1)]
order = [0] * N  
perm(0,M,0)   