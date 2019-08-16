import sys

sys.stdin = open("input2.txt", "r")
def P(s):
    for i in range(len(s)//2):
        if s[i] =='*' or s[-1-i] == '*':
            return 'Exist'
        if s[i] != s[-1-i]:
            return 'Not exist'
    return 'Exist'
 
T = int(input())
for tc in range(1, T+1):
    s = input()
    print(f'#{tc} {P(s)}')

        


