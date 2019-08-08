T = int(input())

def bs(v,p):   
    s=1
    e=p 
    c=0
    while s<=v:       
        m=(s+e)//2
        if m==v:
            return c
        elif m<v:
            s=m 
        else:
            e=m
        c+=1    
    return c

for test_case in range(1, T + 1):
    P,A,B=map(int,input().split())    
    a=bs(A,P)   
    b=bs(B,P)
  
    if a>b:
        print("#{} B".format(test_case))
    elif a<b:
        print("#{} A".format(test_case))
    else:
        print("#{} 0".format(test_case))