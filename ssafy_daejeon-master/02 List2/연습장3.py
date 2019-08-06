def BitPrint(n):
    for i in range(7, -1, -1): # 7부터 0까지. 마지막은 -1 -(-1)
        print(1 if (n & (1 << i)) else 0, end="")
    print()


print(BitPrint(-6))
print(BitPrint(6))
