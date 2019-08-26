arr = 'ABC'
N = len(arr)



for i in range(N):
    for j in range(N):
        if i == j:continue
        for k in range(N):
            if k == j or k == i:continue
            print(arr[i],arr[j],arr[k])
