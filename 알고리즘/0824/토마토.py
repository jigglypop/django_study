# import pprint
from collections import deque
# import sys

def BFS(Q):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    while Q: 
        sy,sx = Q.popleft()               
        for i in range(4):                      
            ny = sy + dy[i]
            nx = sx + dx[i]
            if m[ny][nx] != 0:
                continue          
            m[ny][nx] = m[sy][sx] + 1                        
            Q.append([ny,nx])
def A():
    r = 0
    for y in range(N+2):
        for x in range(M+2): 
            if m[y][x] > r:
                r = m[y][x]
            elif m[y][x] == 0:
                return -1
    return r-1

# sys.stdin = open('input6.txt','r')
M,N = map(int,input().split())
m = [[-1]*(M+2)] + [[-1] + list(map(int,input().split())) + [-1] for _ in range(N)] + [[-1]*(M+2)]
q = deque()
for y in range(N+2):
    for x in range(M+2):
        if m[y][x] == 1:
            q.append((y,x))

BFS(q)                
print(A())
