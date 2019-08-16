import sys

sys.stdin = open("input1.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    n = list(input())
    m = int(len(n)//2)
    a = 'Exist'
    for i in range(m):
        if n[i] != n[len(n)-1-i] and n[i] != '?' and n[len(n)-1-i] != '?':
            a = 'Not exist'
            break     
    print(f'#{tc} {a}')
