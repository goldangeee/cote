def solution(a, b, c, d):
    my_list = [a,b,c,d]
    my_set = set(my_list)
    
    if len(my_set) == 4:
        return min(my_set)
    elif len(my_set) == 1:
        return 1111 * a
    elif len(my_set) == 3:
        score = 1
        for m in my_set:
            if my_list.count(m) == 1:
                score *= m
        return score
    else:
        myset_to_list = list(my_set)
        
        if my_list.count(myset_to_list[0]) == 2:
            p = myset_to_list[0]
            q = myset_to_list[1]
            return (p + q)*(abs(p - q))
        
        else:
            for m in my_set:
                if my_list.count(m) == 1:
                    q = m
                else:
                    p = m
            return (10 * p + q)**2