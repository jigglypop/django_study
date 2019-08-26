# import sys

# sys.stdin = open('input (21).txt', 'r')
# for tc in range(1,11):

def BFS(s):
    r = [] 
    while s:
        v = s.pop(0)
        
        if (not F[v]) or set(r) & set(F[v]) == set(F[v]): 
                        # r에 전것이 다 있을 때           
            r.append(v)
            for i in G[v]:
                if i not in s:
                    s.append(i)     
        else: 
            s.append(v)

    return ' '.join(map(str,r))

for i in range(1,11):  
    V,E = map(int,input().split())
    m = list(map(int,input().split()))

    F = [[] for _ in range(V+1)]
    G = [[] for _ in range(V+1)]
    M = [[] for _ in range(E)]

    visit = [False for _ in range(V+1)]
    for i in range(len(m)):
        M[i//2].append(m[i])

    for w in M:
        F[w[1]].append(w[0])
        G[w[0]].append(w[1])

    s = []
    for i in range(1,len(F)):
        if not F[i]:
            s.append(i)


    # F[0] = 'F'
    # G[0] = 'G'
    # p = list(range(E+1))
    # for i in range(E+1):
    #     print(f'{p[i]} --> {F[i]}:{G[i]}')
    print(f'#{i} {BFS(s)}')