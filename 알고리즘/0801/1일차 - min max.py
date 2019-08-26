T = int(input())
for tc in range(1, T + 1):
    m=int(input())
    n=list(map(int,input().split()))
    print(f'#{tc} {max(n)-min(n)}')