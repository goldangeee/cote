from itertools import permutations as perm

def solution(numbers):
    
    my_list = []
    for n in range(1,len(numbers)+1):
        for p in perm(numbers, n):
            my_list.append(int(''.join(map(str, p))))
    my_list = list(set(my_list))
    for x in [0,1]:
        if x in my_list:
            my_list.remove(x)
            
    cnt = 0    
    for m in my_list:
        for i in range(2,int(m**(0.5))+1):
            if m % i == 0:
                break
        else:
            cnt += 1
    return cnt