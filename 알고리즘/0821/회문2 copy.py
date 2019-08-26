for tc in range(1,11):
    N = int(input())
    arr = [input() for _ in range(100)]

    ans = 1              # 지금까지 찾은 최대 길이
    for idx in range(100):
        for x in range(100):
            # 길이가 짝수
            l,r,cnt = x, x+1, 0
            while l >= 0 and r<100:
                if arr[idx][l] != arr[idx][r]:break
                    l,r,cnt = l-1,r+1,cnt+2
            ans = max(ans,cnt)

            l,r,cnt = x, x+1, 0
            while l >= 0 and r<100:
                if arr[l][idx] != arr[r][idx]:break
                    l,r,cnt = l-1,r+1,cnt+2
            ans = max(ans,cnt)

            # 길이가 홀수
            l,r,cnt = x, x+1, 1
            while l >= 0 and r<100:
                if arr[idx][l] != arr[idx][r]:break
                    l,r,cnt = l-1,r+1,cnt+2
            ans = max(ans,cnt)

            l,r,cnt = x, x+1, 1
            while l >= 0 and r<100:
                if arr[l][idx] != arr[r][idx]:break
                    l,r,cnt = l-1,r+1,cnt+2
            ans = max(ans,cnt)

    print(ans)