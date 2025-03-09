# 송용진
def solution(k, tangerine):
    # 귤의 종류와 개수를 저장할 딕셔너리
    count = {}
    
    # 귤의 종류와 개수를 세기
    for t in tangerine:
        if t in count:
            count[t] += 1
        else:
            count[t] = 1
    
    # 귤의 개수만 추출하고 내림차순으로 정렬
    cnt = sorted(count.values(), reverse=True)
    
    sum_count = 0
    for i, v in enumerate(cnt):
        sum_count += v
        if sum_count >= k:
            return i + 1  # 필요한 종류의 수 반환

    return len(cnt)  # 만약 k보다 작은 경우 모든 종류를 반환
