def solution(l, r):
    answer = []
    
    my_list = list(set([i for i in range(0,10)]) - set([0,5]))
    
    for target in [5*i for i in range(l//5,r//5+1)]:
        tmp = True
        for m in my_list:
            if str(m) in str(target):
                tmp = False
                break
        if tmp == False:
            continue
        else:
            answer.append(target)
    if answer:    
        return answer
    else:
        return [-1]