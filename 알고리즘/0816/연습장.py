import sys

sys.stdin = open("input1.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    n = list(input())
    m = 20-len(n)
    f = 'Exist'
    if '*' not in n:
        a = ''.join(n)
        b = ''.join(reversed(n))
        if a != b:
            f = 'Not exist'
    else:
        for i in range(m):
            n.insert(n.index('*'),'*')
        for i in range(len(n)):
            if n[i] != n[-1-i] and n[i] != '*' and n[-1-i] != '*':
                f = 'Not exist'
                break
    print(f'#{tc} {f}')




    