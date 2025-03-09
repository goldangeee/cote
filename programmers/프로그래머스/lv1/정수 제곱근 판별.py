# 송용진
def solution(n):
    x = n ** 0.5 # n의 양의 제곱근 x를 구한다
    if x == int(x) and x > 0: # x가 양의 정수인지 확인한다
        return (x + 1) ** 2
    else:
        return -1