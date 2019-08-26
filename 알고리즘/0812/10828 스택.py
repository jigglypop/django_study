def push(a):
    return s.append(a)
def top(s):
    if len(s) == 0:
        return -1
    else:
        return s[-1]
def size(s):
    return len(s)
def empty(s):
    if len(s) == 0:
        return 1
    else:
        return 0
def pop(s):
    if len(s) == 0:
        return -1
    else:
        return s.pop()


T = int(input())
s = []
for i in range(T):
    m = list(input().split())
    
    # if m[0] == 'push':
    #     push(m[1])
    # elif m[0] == 'top':
    #     print(top(s))
    # elif m[0] == 'size':
    #     print(size(s))
    # elif m[0] == 'empty':
    #     print(empty(s))
    # elif m[0] == 'pop':
    #     print(pop(s))
    
