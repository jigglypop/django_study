# for tc in range(1,11):
#     n = int(input())
#     arr = [list(map(int,input().split())) for _ in range(100)]
    
#     Max = 0
#     for i in range(100):
#         S = 0
#         for j in range(100):
#             S += arr[i][j]
#         Max = max(Max,S)

#     S = 0
#     for i in range(100):
#         S += arr[i][i]
#     Max = max(Max,S)

#     S = 0
#     for i in range(100):
#         S += arr[i][99-i]
#     Max = max(Max,S)


for tc in range(1,11):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    
    Max = 0
    dsum1 = dsum2 = 0
    for i in range(100):
        rsum = csum = 0
        dsum1 += arr[i][i]
        dsum2 += arr[i][99-i]
        for j in range(100):
            rsum += arr[i][j]
            csum += arr[j][i]
   


    Max = max(Max,S)