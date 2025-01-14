# 명예의 전당 (1)
def solution(k, score):
    answer = []
    hof = [] # 명예의 전당
    
    for i in range(len(score)):
        hof.append(score[i]) # 명예의 전당에 일단 추가
        if len(hof) != 1: # 명예의 전당에 한 명 있을 때를 제외하고 내림차순 정렬
            hof.sort(reverse=True)
            
        if len(hof) >=  k: # 명예의 전당이 k명 초과일 경우 상위 k명 슬라이싱 
            hof = hof[:k]
        answer.append(hof[-1])# 당일 발표 점수 추가 
            
    return answer

'''
def solution(k, score):
    q = []
    answer = []
    for s in score:
        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))

    return answer
'''
# 명예의 전당의 순위가 공개되는 것이 아니기 때문에
# 굳이 sort하고 슬라이싱할 필요없이
# 최소값을 제거하고 최소값을 점수 공개하면됨