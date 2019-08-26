import pprint
from collections import deque
from sys import stdin
input = stdin.readline

def BFS(Q):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    while Q: 
        sy,sx,v = Q.popleft()               
        for i in range(4):                      
            ny = sy + dy[i]
            nx = sx + dx[i]
            if m[ny][nx] != '0' or (m[ny][nx] == '1' and v == False):
                continue
            elif m[ny][nx] =='1' and v == True:
                m[ny][nx] = str(int(m[sy][sx]) + 1) 
                print(Q)                    
                Q.append([ny,nx,False]) 
            else:
                m[ny][nx] = str(int(m[sy][sx]) + 1)
                print(Q)                     
                Q.append([ny,nx,v])                
            # m[ny][nx] = str(int(m[sy][sx]) + 1)                   
            # Q.append([ny,nx,v])
        
N,M = map(int,input().split())
m = [['-1']*(M+2)] + [['-1'] + list(input()) for _ in range(N)] + [['-1']*(M+2)]
visit = [[0]*(M+2) for _ in range(N+2)]

q = deque()
q.append([1,1,True])
m[1][1] = '1'
BFS(q) 
pprint.pprint(m)
if m[N][M] == '0' or m[N][M] == '1':
    print(-1)
else:
    print(m[N][M])

         

