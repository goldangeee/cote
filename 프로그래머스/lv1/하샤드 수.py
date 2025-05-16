# 송용진
def solution(x):
    sum = 0 # 모든 자릿수의 합
    for i in str(x):
        sum += int(i)
        
    return True if x % sum == 0 else False