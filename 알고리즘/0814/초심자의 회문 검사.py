# T = int(input())

# for tc in range(1, T+1):
#     n = list(input())
#     m = [i for i in n]
#     m.reverse()
    
#     N ="".join(n)
#     M ="".join(m)
    
#     if M == N:
#         print(f'#{tc} 1')
#     else:
#         print(f'#{tc} 0')


for tc in range(1, int(input())+1):
    N =input()
    M =N[::-1]
    print(f'#{tc} {int(M == N)}')