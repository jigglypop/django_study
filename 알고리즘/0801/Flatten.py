for tc in range(1,11):
    T = int(input())
    m = list(map(int,input().split()))
    up = [0]   
    # up은 위에 쌓여있는 블록의 수를 구하는 것.
    # up은 전의것 + 해당 줄에서 새로 추가된 것 순서대로 추가해야 하기 때문에
    # 초기값 0이 들어가지 않으면 범위 오류가 남
    
    for i in range(100,0,-1):    
        up.append(up[100-i] + m.count(i))
    down = [100-up[::-1][i] for i in range(101)]
    # down은 100에 up의 순서를 반대로 해서 빼주면 순서대로 정렬된다. 
    # down은 1층부터 빈 공백의 갯수를 구하는 것
 
    # max_sum에 하나씩 더하고, T를 초과하면 해당값을 반환한다.
    max_sum = 0
    for up_num in range(1,101):
        max_sum += up[up_num]
        if max_sum > T:
            break
    # min_sum에 하나씩 더하고, T를 초과하면 해당값을 반환한다.
    min_sum = 0
    for down_num in range(100):
        min_sum += down[down_num]
        if min_sum > T:
            break
 
    print(f'#{tc} {((100-up_num)-down_num+1)}')
    # up은 위에서부터 센 것이므로 100에 빼준다.
    

