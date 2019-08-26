T = int(input())
for t in range(1, T+1):
    n = list(input())   
    s = []
    
    for i in range(len(n)):      
        if not s or s[-1] != n[i]:
            s.append(n[i])
        elif s and s[-1] == n[i]:
            s.pop()
    print(f'#{t} {len(s)}')