def solution(n):
    my_list = []
    sqrt_n = n ** 0.5
    for i in range (1,int(sqrt_n)+1):
        if n % i == 0:
            my_list.append(i)
            my_list.append(n/i)
    return sum(set(my_list))