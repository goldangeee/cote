# 송용진
'''
최대한 많은 부서를 지원해야하므로
적은 예산을 신청한 부서부터 순차적으로 지원
'''
def solution(d, budget):
    answer = 0
    d.sort()
    for x in d:
        if x <= budget:
            budget -= x
            answer += 1
        else:
            break
    return answer