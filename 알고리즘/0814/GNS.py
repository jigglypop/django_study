T = int(input())
for tc in range(1,T+1):
    n,t = list(input().split())
    m = list(input().split())
    print(len(m))
    r = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    s = [0]*10
    for i in m:
        if i in r:
            a = r.index(i)
            s[a] += 1
    R = ''
    for i in range(10):
        print(f'{r[i]*s[i]} ',end="")
    


