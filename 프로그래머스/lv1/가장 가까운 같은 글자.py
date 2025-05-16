# 가장 가까운 같은 글자
def solution(s):
    answer = []
    for i,v in enumerate(s):
        if i == 0:
            answer.append(-1)
        else:
            tmp = s[:i]
            if v not in tmp:
                answer.append(-1)
            else:
                hubo = []
                for j,t in enumerate(tmp):
                    if t == v:
                        hubo.append(j)
                answer.append(i-max(hubo))
    return answer
'''
def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i
    return answer
'''