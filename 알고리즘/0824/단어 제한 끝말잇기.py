# import sys
# import pprint

# sys.stdin = open('input3.txt','r')
# C = int(input())
# for tc in range(C):
#     n = int(input())
#     m = []
#     for _ in range(n):
#         a = list(input())
#         m.append([a[0],a[-1]])
#     print(m)
#     r = []
#     for i in range(n):
#         for j in range(2):
#             if m[i][j] not in r:
#                 r.append(m[i][j])
#     R = list(enumerate(r))
#     G = [[] for _ in range(len(r)+1)]
#     for i in range(len(r))