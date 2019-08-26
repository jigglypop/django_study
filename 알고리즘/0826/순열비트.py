arr = 'ABC'
N = len(arr)
order = [0] * N
def perm(k,n,visit):
    if k == n:
        for i in range(N):
            print(arr[order[i]], end=' ')
        print()
    else:
        # 아직 선택되지 않은 요소들을 찾는다.
        for i in range(n):
            if visit & (1<<i): continue
            order[k] = i
            perm(k+1,n, visit|(1<<i))
perm(0,N,0)