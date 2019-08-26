T = int(input())
for tc in range(1,T+1):
    n = int(input())
    N = [[0]*10 for _ in range(10)]
    for i in range(n):
        m = list(map(int,input().split()))
        for y in range(m[0], m[2]+1):
            for x in range(m[1], m[3]+1):
                if m[4] == 1:
                    N[y][x] += 1
                else:
                    N[y][x] += 2
    r = 0
    for y in range(10):
        for x in range(10):
            if N[y][x] == 3:
                r += 1
    print(f'#{tc} {r}')