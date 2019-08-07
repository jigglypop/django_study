arr = [64, 25, 10, 22, 11]

# 첫번째 단계 [0,n-1] / n까지 해도 상관없으나 속도가 느리고 의미없다.
m = 0
for i in range(len(arr)):
    m = i
    for j in range(i+1,len(arr)):
        if arr[m] > arr[j]:
            m = j 
    arr[i],arr[m] = arr[m],arr[i]
print(arr)
