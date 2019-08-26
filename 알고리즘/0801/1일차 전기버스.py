T = int(input())

for tc in range(1,T+1):
    K,M,N=list(map(int,input().split()))
    m=list(map(int,input().split()))
    
    
    n=0
    p=0
    k=K
    while p<M:
        if p+k>=M:
            break
        elif p+k in m:
            p+=k
            n+=1
            k=K
        else:
            k-=1
            if k==0:
                n=0
                break
     
    print(f'#{tc} {n}')