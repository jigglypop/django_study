def F(a):
    r = [a[0]]
    c = [0]
    for i in range(len(a)):
        if a[i] != r[-1]:
            r.append(a[i])
            c.append(1)
        else:
            c[-1] += 1
    d = [[0]*2 for _ in range(len(r))]
    for i in range(len(r)):
            d[i][0] = r[i]
            d[i][1] = c[i]

    if len(d) == 1:
        return 1

    i = 1    
    while i != len(d):
        if (d[i][1] < X and d[i][0] != max(r)) or d[i-1][0] - d[i][0] > 1 or d[i-1][0] - d[i][0] < -1:
            print(d)
            return 0
        elif d[i-1][0] - d[i][0] == 1:
            d[i][1] -= X
            i += 1
        elif d[i-1][0] - d[i][0] == -1:
            if d[i-1][1] < X:
                print(d)
                return 0
            else:
                i += 1
    
    return 1    


        # if d[i][0] != M and d[i][1] < X:            
        #     return 0
        # elif i != 0 or i != len(d)-1:
        #     if 



# T = int(input())
# for tc in range(1,T+1):
N, X = list(map(int,input().split()))

# 가로
mx = [list(map(int,input().split())) for _ in range(N)]
# 세로
my = [[0]*N for _ in range(N)]
for y in range(N):
    for x in range(N):
        my[y][x] = mx[x][y]

R = 0
for i in mx:
    R += F(i)
for i in my:
    R += F(i)

print(f'# {R}')

 



