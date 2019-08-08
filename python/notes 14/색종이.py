n = int(input())
M = [list(map(int,input().split())) for _ in range(n)]
s = [[0]*101 for _ in range(101)]

c = 0
for m in M:   
    c += 1
    for y in range(m[0],m[0]+m[2]):
        for x in range(m[1],m[1]+m[3]):            
            s[y][x] = c

for i in range(1,c+1):
    Sum = 0
    for y in range(101):
        for x in range(101):
            if s[y][x] == i:
                Sum += 1
    print(Sum)


# for i in range(1,c+1):
#     Sum = 0
#     for y in range(11):
#         for x in range(11):
#             if s[y][x] == i:
#                 Sum += 1





