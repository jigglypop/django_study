import sys

sys.stdin = open("input4.txt", "r")
def M(v,a):
    i = a[1] -1
    while T - 1 >= i:      
        if v[i] == 1:
            v[i] = 0        
        else:
            v[i] = 1
        i += a[1]
    return v

def F(v,a):
    t = a[1] - 1
    g = [a[1] - 1, len(v) - a[1]]
    c = [t - min(g), t + min(g)] 
    for i in range(min(g)+1):
        if v[t-i] == v[t+i]:
            continue
        else:
            c[0] = t - i + 1 
            c[1] = t + i - 1 
            break   
    for i in range(c[0],c[1]+1):
        if v[i] == 1:
            v[i] = 0        
        else:
            v[i] = 1
    return v


T = int(input())
v = list(map(int,input().split()))
n = int(input())
m = [list(map(int,input().split())) for _ in range(n)]

for i in range(len(m)):
    if m[i][0] == 1:
        M(v,m[i])
    else:
        F(v,m[i])

for i, e in enumerate(v[1:]):
    if i and not(i % 20):
        print()
    print(e,end=" ")
