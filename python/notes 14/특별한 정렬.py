T = int(input())
for tc in range(1, T + 1):
    n=int(input())
    m=list(map(int,input().split()))
    m.sort(reverse=True)
    r = []
    d = ([0,-1] * int(len(m)/2) + [-1]) if len(m) % 2 else [0,-1] * int(len(m)/2)
    for i in d:
        r.append(str(m.pop(i)))
    a = ' '.join(r[:10])
    print(f'#{tc} {a}')