import pprint


def D(m,r):
    for k in range(len(m)):
        if r[-1][1] == m[k][0]:
            r.append(m.pop(k))
            return D(m,r)        
    return r

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    m = list(map(int,input().split()))
    M = []
    s = [[0]*(max(m)+1) for _ in range(max(m)+1)]

    for i in range(0,n*2,2):
        M.append([m[i],m[i+1]])

    R = []
    c = []
    for i in range(len(M)):
        m = M[:]
        r = [M[i]]
        R.append(D(m,r))  
        c.append(len(D(m,r)))

    a = c.index(max(c))
    A = R[a]

    w = ''
    for i in A: 
        for j in range(2):       
            w += ' '+str(i[j])

    print(f'#{tc}{w}')




        
    