T= int(input())
for t in range(1,T+1):
    n = list(input())
    m=R(n)
        
    s=[]
    for k in range(len(m)):
        if not s : s.append(m[k])
        else :
            if m[k]==")" and s[-1]=="(" : s.pop()
            elif m[k]=="}" and s[-1]=="{" : s.pop()
            else : s.append(m[k])     
            
    if len(s)==0:
        a="1"
    else:
        a="0"
                    
    print(f'#{t} {a}')