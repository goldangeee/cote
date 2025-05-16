# 3진법 뒤집기
def solution(n):
    answer = 0
    my_list = []
    while n >= 3:
        my_list.append(n % 3)
        n //= 3
    my_list.append(n)
    len_m = len(my_list)
    for idx,v in enumerate(my_list):
        answer += v * 3 ** (len_m-1-idx)
    return answer