def bs(P,A):
    l = 1
    r = P
    cnt = 0 
    c = 0   
    while c != A :
        c = int((l+r)/2)
        if c == A:
            return cnt
        elif A < c:
            cnt += 1 
            r = c 
        elif c < A:
            cnt += 1
            l = c
    return cnt

T = int(input())
for tc in range(1,T+1):
    P,A,B = list(map(int, input().split()))
    if bs(P,A) > bs(P,B):
        print(f'#{tc} B')
    elif bs(P,A) < bs(P,B):
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')




