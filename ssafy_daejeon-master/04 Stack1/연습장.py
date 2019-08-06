class Stack:
    def __init__(self,size):
        self.size = size
        self.arr = [0] * size
        self.top = -1
    def push(self, item):
        self.top += 1
        self.arr[self.top] = item

    
S = Stack(10)

print(S.arr)
for i in range(5):
    S.push(i)
print(S.arr)