# 다음에 올 숫자
def solution(common):
    tmp = []
    for i,v in enumerate(common):
        if i != 0:
            tmp.append(v - common[i-1])
    if len(set(tmp)) == 1:
        return common[-1]+tmp[0]
    else:
        return common[-1] * common[1] / common[0]

# 다른 사람의 풀이
# def solution(common):
#     answer = 0
#     a,b,c = common[:3]
#     if (b-a) == (c-b):
#         return common[-1]+(b-a)
#     else:
#         return common[-1] * (b//a)
#     return answer