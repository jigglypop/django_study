import sys

sys.stdin = open("input (19).txt", "r")
for tc in range(1,11):
    T = int(input())
    v = list(input())
    n = v.count('+')
    for i in range(n):
        v.remove('+')
    s = [v[0]]
    for i in range(1,len(v)):        
        if s[-1] == '*':
            s.pop()
            n = s.pop()
            s.append(int(n) * int(v[i]))
        else:
            s.append(v[i])
    r = []
    for i in s:
        if type(i) == str:
            r.append(int(i))
        else:
            r.append(i)

    print(f'#{tc} {sum(r)}')