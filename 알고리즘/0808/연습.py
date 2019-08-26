
n = [1,2,3,4,5,6]
# 0 0 0 0 0 0
# 

for i in range(1<<len(n)):
    for j in range(len(n)):
        if i & (1<<j) ==1:
            print(n[j], end = '')
    print()

