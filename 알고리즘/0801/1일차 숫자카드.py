T = int(input())
for tc in range(1, T + 1):
    n=int(input())
    m=list(map(int,input()))
    
    a=-1
    c=0
    
    for i in range(10):
        if m.count(i)>=c:
            a=i
            c=m.count(i)
     
    print(f'#{tc} {a} {c}')