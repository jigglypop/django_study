T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    n = [i for i in range(1, 13)]
    
    r = []
    for i in range(1 << len(n)):
        s = []
        for j in range(len(n)):            
            if i & (1 << j):
                s.append(n[j])
        if len(s) == N:
            r.append(sum(s))
    
    print(r)
    h = 1 if K in r else 0
    print(f'#{tc} {h}')
             