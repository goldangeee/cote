def solution(citations):
    citations.sort(reverse=True)  # 인용 횟수를 내림차순으로 정렬
    for i in range(len(citations)):
        if citations[i] <= i:  # i편 이상의 논문이 i회 이상 인용된 경우
            return i
    return len(citations)
'''
내림차순 정렬되어있기 때문에
i번째  논문이 i 이하일 경우
i이하인 논문이 i개이기 때문에
i가 정답
'''