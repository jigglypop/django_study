import sys
from collections import deque
import pprint

def BFS(s):
    m[s[0]][s[1]] = 1
    Q = deque()
    Q.append(s)
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    while Q:
        sy,sx = Q.popleft()
        for i in range(4):            
            ny = sy + dy[i]
            nx = sx + dx[i]
            if 0 <= ny < Y and 0 <= nx < X:
                if m[ny][nx] == 'L':
                    m[ny][nx] = m[sy][sx] + 1
                    Q.append([ny,nx])

sys.stdin = open('input3.txt','r')
Y,X= map(int,input().split()) 
m = [list(sys.stdin.readline().strip()) for _ in range(Y)]

s = [1,0]
BFS(s)
# for y in range(Y):
#     for x in range(X):
#         if m[y][x] == 'L':
#             v = [y,x]
pprint.pprint(m)
