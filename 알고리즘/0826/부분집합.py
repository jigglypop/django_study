arr = 'ABC'
bits = [0] * len(arr)

def subset(k,n):        # k: 현재 노드의 높이, n: 단말 노드의 높이
    if k == n:
        for i in range(n):
            if bits[i]:
                print(arr[i],end=' ')
            print()
    bits[k] = 1 
    subset(k+1,n)
    bits[k] = 0
    subset(k+1,n)
subset(0,3)             # 0: 초기, 어떤 선택도 하지 않았다.
                        # 3: 해야할 선택의 횟수

