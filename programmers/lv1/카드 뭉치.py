# 카드 뭉치
def solution(cards1, cards2, goal):
    cards1,cards2 = cards1[::-1],cards2[::-1]# pop사용을 위해 리스트를 전부 뒤집어준다.
    for g in goal:
        if cards1:# 빈 리스트가 아닐 경우
            if g == cards1[-1]:#마지막 카드가 goal 단어와 일치할 경우 pop하고 다음 goal 단어로 이동
                cards1.pop()
                continue
        if cards2:
            if g == cards2[-1]:
                cards2.pop()
                continue
        return "No" # goal단어와 일치하는 카드가 없을 때
    return "Yes"# goal 단어들과 일치하는 카드들이 모두 있을 때
'''
def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) >0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"
'''
'''
1. pop(0)를 사용하면 리스트를 뒤집을 필요가 없다.
2. g == cards1[0]의 and 앞에 조건문이 있으면 if 문을 적게 쓸 수 있다.
'''
