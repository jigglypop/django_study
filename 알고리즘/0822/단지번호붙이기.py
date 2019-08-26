import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(sys.stdin.readline())
a = [list(sys.stdin.readline()) for _ in range(n)]
c = 0
apt = []


def DFS(x, y):
    global c
    a[x][y] = '0'
    c += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if a[nx][ny] == '1':
            DFS(nx, ny)
            
for i in range(n):
    for j in range(n):
        if a[i][j] == '1':
            c = 0
            DFS(i, j)
            apt.append(c)
print(apt)
print(len(apt))
apt.sort()
for i in apt:
    print(i)




