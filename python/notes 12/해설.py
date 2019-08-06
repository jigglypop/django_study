def a_c(word):
    # 결과 통
    result ={}
    for char in word:
        if char in word:
            # 알파벳이 있으면, -1
            if char in result.keys():
                result[char] += 1
            # 없으면, 1
            else:
                result[char] = 1
        return result
    



print(a_c('hello')) # -> {'h':1, 'e':1, 'l':2, 'o':1}