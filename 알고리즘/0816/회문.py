for t in range(int(input())):
    n, m = list(map(int, input().split()))
    rows_arr = [input() for i in range(n)]
    cols_arr = list(map(''.join, list(zip(*rows_arr))))
    result = list()
    stride = 1
    iteration = int((n-m)/stride) + 1

    for str1, str2 in zip(rows_arr, cols_arr):
        for i in range(iteration):
            if m % 2 == 0:
                s1_f = str1[i:i+int(m / 2)]
                s1_b = str1[i+int(m / 2):i+2*int(m / 2)]
                s2_f = str2[i:i+int(m / 2)]
                s2_b = str2[i+int(m / 2):i+2*int(m / 2)]
                if s1_f == s1_b[::-1]:
                    result.append(str1[i:i+2*int(m / 2)])
                    break
                if s2_f == s2_b[::-1]:
                    result.append(str2[i:i+2*int(m / 2)])
                    break

            else:
                s1_f = str1[i:i+int(m / 2)]
                s1_b = str1[i+int(m / 2)+1:i+2*int(m / 2)+1]
                s2_f = str2[i:i+int(m / 2)]
                s2_b = str2[i+int(m / 2)+1:i+2*int(m / 2)+1]
                if s1_f == s1_b[::-1]:
                    result.append(str1[i:i+2*int(m / 2)+1])
                    break
                if s2_f == s2_b[::-1]:
                    result.append(str2[i:i+2*int(m / 2)+1])
                    break
        if len(result) == 1:
            break
    print("#{} {}".format(t+1, result[0]))