import sys


sys.stdin = open('input.txt','r')
V,E = map(int,sys.stdin.readline().split())
m = [list(input()) for _ in range(V)]
   
print(m)
