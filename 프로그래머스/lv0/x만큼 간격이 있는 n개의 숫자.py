# 송용진
# 0단계 같은 1단계
def solution(x, n):
    answer = []
    start = x
    for _ in range(n):
        answer.append(start)
        start += x
    return answer