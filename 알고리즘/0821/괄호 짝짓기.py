def F(v):
    A = ['{','[','(','<']
    B = ['}',']',')','>']
    s = []
    for w in v:
        if w in A:
            s.append(w)
        elif w in B:
            m = B.index(w)
            if s[-1] == A[m]:
                s.pop()
            else:
                return 0
    if len(s)>0:
        return 0
    return 1


# import sys
# sys.stdin = open('input (16).txt','r')
for tc in range(1,11):
    T = int(input())
    v = list(input())

    print(f'#{tc} {F(v)}')
    
              

    
            

    


