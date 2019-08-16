T = int(input())
for tc in range(1, T + 1):
    n = input()
    m = list(input())
    h = []
    for i in range(len(m)-len(n)+1):
        s = m[i:i+len(n)]
        a = "".join(s)
        h.append(a)
    print(h)
    print(f'#{tc} {int(n in h)}')
