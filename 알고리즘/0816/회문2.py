# import sys
# import pprint

def P(x):
    for n in range(100,0,-1):
        h = []
        k = []
        for i in range(100-n+1):
            y = x[i:i+n]
            h.append(''.join(y))
            k.append(''.join(reversed(y)))
        for i in range(len(h)):
            if h[i] == k[i]:
                return n

#sys.stdin = open("input (14).txt", "r")

m = int(input())
w = [list(input()) for _ in range(100)]
wr = [[0]*100 for _ in range(100)]

for y in range(100):
    for x in range(100):
        wr[y][x] = w[x][y]

W = w + wr

r = 0
for i in W:
    if P(i) > r:
        r = P(i)
print(f'#{m} {r}')
