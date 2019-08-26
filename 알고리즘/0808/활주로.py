# def S(mx,M,N):
#     dx = []
#     for j in range(N) :
#         r = []
#         for i in range(N):
#             if mx[j][i] == M:
#                 r.append(i)
#         if len(r) == 0:
#             dx.append([0,0])
#         else:
#             R = [r[0],r[-1]]
#             dx.append(R)


# m = 3 3 3 2 1 1
# dx = [0, 2]
# i 


def S(m,i,dx):   
    if dx[0] - dx[1] == N - 1:
        return 1
    elif dx[0] == 0:
        if dx[1] + 1 < N-1 and m[dx[1] + 1] == i:
            dx[1] += 1
    


        

# T = int(input())
# for tc in range(1,T+1):

N, X = list(map(int,input().split()))
mx = [list(map(int,input().split())) for i in range(N)]
my = [[0]*N for _ in range(N)]
for y in range(N):
    for x in range(N):
        my[y][x] = mx[x][y]

M = 0
for y in range(N):
    for x in range(N):
        if mx[y][x] >= M:
            M = mx[y][x]

dx = []
R = []
for j in range(N) :
    r = []
    for i in range(N):
        if mx[j][i] == M:
            r.append(i)
    if len(r) == 0:
        dx.append([0,0])
    else:
        R = [r[0],r[-1]]
        dx.append(R)

    



