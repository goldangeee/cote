# 겹치는 선분의 길이
def solution(lines):
    def my_func(x):
        res = []
        for i in range(x[0],x[1]+1):
            res.append((i,i+1))
            if i+1 == x[1]:
                break
        return res
    
    A = set(my_func(lines[0]))
    B = set(my_func(lines[1]))
    C = set(my_func(lines[2]))
    
    return len((A & B) | (B & C) | (A & C))
# 다른 풀이
# def solution(lines):
#     sets = [set(range(min(l), max(l))) for l in lines]
#     return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])