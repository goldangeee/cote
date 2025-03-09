def solution(arr):
    key = len(arr) - len(arr[0])
    if key > 0:
        for i in arr:
            for _ in range(key):
                i.append(0)
    elif key < 0:
        tmp = []
        for _ in range(len(arr[0])):
            tmp.append(0)
        for _ in range(abs(key)):
            arr.append(tmp)
    return arr