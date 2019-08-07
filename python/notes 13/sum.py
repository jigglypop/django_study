for tc in range(1,11):
    n = int(input())
    m = []
    for i in range(100):
    	m.append(list(map(int,input().split())))   
    
    sum1 = 0
    sum2 = 0
    c = 1
    x1 = 0
    for y1 in range(100):        
        sum1 += m[y1][x1]
        sum2 += m[y1][99-x1]
        x1 += 1   
    sum3 = []
    for y2 in range(100):
        sumH = 0
        for x2 in range(100):
            sumH += m[y2][x2]
        sum3.append(sumH)
    sum4 = []
    for y2 in range(100):
        sumV = 0
        for x2 in range(100):
            sumV += m[x2][y2]
        sum4.append(sumV)
    
    print(f'#{n} {max(sum1,sum2,max(sum3),max(sum4))}')