arr = [2, 5, 7, 8, 12, 16, 21, 23, 33, 39, 42, 45, 45, 49, 62, 88]

def sequence_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return '없음'

print(sequence_search(arr, 888))