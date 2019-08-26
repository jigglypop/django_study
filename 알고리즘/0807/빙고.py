m = []
for i in range(5):
    a = list(map(int,input().split()))
    m.append(a)
r = []
for i in range(5):
    b = list(map(int,input().split()))
    r.append(b)


s = [[0]*5 for _ in range(5)]
c = 0

for yr in range(5):
    for xr in range(5):
        for ym in range(5):
            for xm in range(5):
                if m[ym][xm] == r[yr][xr]:
                    s[ym][xm] = c
                    c += 1
re =[]                    
re.append([s[0][0],s[1][1],s[2][2],s[3][3],s[4][4]])
re.append([s[4][0],s[3][1],s[2][2],s[1][3],s[0][4]])

for yi in range(5):
    a = []
    for xi in range(5):
        a.append(s[yi][xi])
    re.append(a)
for yj in range(5):
    b = []
    for xj in range(5):
        b.append(s[xj][yj])
    re.append(b)        

result = []
for su in range(12):
    result.append(sum(re[su]))

final2 = []
for i in range(12):   
    final1 = []
    for j in range(5):
        final1.append(re[i][j])
    final2.append(max(final1))
final2.sort()
print(final2[2]+1)
    
