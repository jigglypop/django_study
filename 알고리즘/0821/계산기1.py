import sys

sys.stdin = open("input (18).txt", "r")
for tc in range(1,11):
    T = int(input())
    v = list(input())
    s = []
    for n in v:
        if n != '+':
            s.append(int(n))
    
    print(f'#{tc} {sum(s)}')

