# 송용진
def solution(numbers):
    ans = set() #중복방지를 위해 set형 자료형을 사용
    for i1,v1 in enumerate(numbers[:-1]): # v1의 최대 범위는 numbers의 마지막 원소를 제외한 나머지
        for v2 in numbers[i1+1:]:# v2의 범위는 i1 인덱스 바로 다음부터 끝까지
            ans.add(v1+v2)
    return sorted(list(ans))