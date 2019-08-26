T = int(input())
for tc in range(1, T + 1):   
    n=list(map(int,input().split()))
    m=list(map(int,input().split()))
    
    a=n[0]-n[1]+1
    s=[]
  
    for i in range(a):                 
        s.append(sum(m[i:i+n[1]]  ))
    x=max(s)-min(s)
    print(f'#{tc} {x}')