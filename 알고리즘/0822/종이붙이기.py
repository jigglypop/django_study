def D(x):
    if x==N:
        return 1
    if x>N:
        return 0
    return D(x+10)+D(x+20)*2

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc} {D(0)}')