T = int(input())
print(f'#{T}')
t = int(input())
S = []
for tc in range(1,t+1):
    a,n = list(input().split())
    for i in range(int(n)):
        S.append(a)


b = S[(len(S)//10)*10:]
print(b)
while len(S) > 10:
    a = S[:10]
    S = S[11:]
    print(''.join(a))
print(''.join(b))


    