# 송용진
def solution(friends, gifts):
    splited_gifts = [[''] * 2 for _ in range(len(gifts))]
    for i,g in enumerate(gifts):
        splited_gifts[i][0],splited_gifts[i][1] = g.split()
    
    res_dict = {}
    for name in friends:
        res_dict[name] = 0
    
    unresolved_gifts = []
    
    #선물득실비교
    for i in range(len(friends)):
        for j in range(i+1,len(friends)):
            fst,sec = 0,0
            for k in splited_gifts:
                # friends[i] # friends[j]
                if k[0] == friends[i] and k[1] == friends[j]:
                    fst += 1
                if k[1] == friends[i] and k[0] == friends[j]:
                    sec += 1
                    
            if fst > sec:
                res_dict[friends[i]] += 1
            elif fst < sec:
                res_dict[friends[j]] += 1
            else:
                unresolved_gifts.append([friends[i],friends[j]])
                
    def gift_index(name):
        point = 0
        for s in splited_gifts:
            if s[0] == name:
                point += 1
            elif s[1] == name:
                point -= 1 
        return point
    
    # 선물득실비교가 불가능한 경우 선물지수비교
    fst,sec = 0,0
    for u in unresolved_gifts:
        #u[0] #u[1]
        if gift_index(u[0]) > gift_index(u[1]):
            res_dict[u[0]] += 1
        elif gift_index(u[0]) < gift_index(u[1]):
            res_dict[u[1]] += 1
            
    return max(res_dict.values())