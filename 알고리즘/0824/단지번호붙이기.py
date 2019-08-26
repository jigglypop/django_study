import sys
import pprint

sys.stdin = open('input2.txt','r')
T = int(input())
m = [['0']*(T+2)] + [['0'] + list(input()) + ['0'] for _ in range(T)] + [['0']*(T+2)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]
c = 0

def DFS(sy,sx): 
    global c
    m[sy][sx] = '0'
    c += 1   
    for i in range(4):
        ny = sy + dy[i]
        nx = sx + dx[i]
        if m[ny][nx] == '1':           
            DFS(ny,nx)

r1 = []
r2 = 0
for y in range(T+2):
    for x in range(T+2):
        if m[y][x] == '1':
            DFS(y,x)
            r1.append(c)
            c = 0
            r2 += 1
            
print(r2)
for i in r1:
    print(i)
