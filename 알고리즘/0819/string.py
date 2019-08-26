for tc in range(1,11):
    T = int(input())
    p = input()
    t = input()

    c = 0
    m, n = len(p), len(t)
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if p[j] != t[i + j]: break
            j += 1
        if j == m:
            c += 1
    print(f'#{T} {c}')      

            
