num_switch = int(input())
s = [0] + input().split()
for _ in range(int(input())):
    data = input().split()
    if data[0] == '1':
        i = int(data[1])
        while(i<num_switch+1):
            if s[i] == '1':
                s[i] = '0'
            elif s[i] == '0':
                s[i] = '1'
            i += int(data[1])
    else:
        i = int(data[1])
        if s[i] == '1':
            s[i] = '0'
        elif s[i] == '0':
            s[i] = '1'
        j = 1
        while(i - j > 0 and i + j < num_switch+1 and s[i+j] == s[i-j]):
            if s[i + j] == '1':
                s[i + j] = '0'
                s[i - j] = '0'
            elif s[i + j] == '0':
                s[i + j] = '1'
                s[i - j] = '1'
            j += 1
for i, e in enumerate(s[1:]):
    if i and not(i % 20):
        print()
    print(e, end=" ")
