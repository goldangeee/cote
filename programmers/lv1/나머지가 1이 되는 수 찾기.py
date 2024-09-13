# 송용진
def solution(n):
    tmp = n - 1
    answer = 2
    while True:
        if tmp % answer == 0:
            break
        answer += 1
    return answer