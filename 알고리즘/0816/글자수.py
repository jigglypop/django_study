T = int(input())

for test_case in range(1, T + 1):
    n=list(input())
    m=list(input())
    s=[]
    for i in range(len(n)):
        a=m.count(n[i])
        s.append(a)
    b=max(s)
    print("#{} {}".format(test_case,b))
    