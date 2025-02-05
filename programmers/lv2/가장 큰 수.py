from functools import cmp_to_key

def my_func(x,y):
    A = str(x)
    B = str(y)
    if int(A+B) > int(B+A):
        return -1
    elif int(A+B) < int(B+A):
        return 1
    else:
        return 0
    
def solution(numbers):
    result = "".join(map(str, sorted(numbers, key=cmp_to_key(my_func))))
    return result if result[0] != '0' else '0'