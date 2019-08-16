import sys
import pprint


def P(x,n):
    h = []
    k = []
    c = 0
    for i in range(8-n+1):
        y = x[i:i+n]
        h.append(''.join(y))
        k.append(''.join(reversed(y)))
    for i in range(len(h)):
        if h[i] == k[i]:
            c += 1
    return c



# sys.stdin = open("input (13).txt", "r")

for tc in range(1, 11):
    n = int(input())
    w = [list(input()) for _ in range(8)]
    wr = [[0]*8 for _ in range(8)]

    for y in range(8):
        for x in range(8):
            wr[y][x] = w[x][y]


    r = 0
    for i in range(8):
        r += P(w[i],n) + P(wr[i],n)

    print(f'#{tc} {r}')
