def DFS(v):
    if v == 10:       
        return v
    print(v)
    return DFS(v+1)

print(DFS(1))