# 송용진
def solution(left, right):
    ans = 0 # 결과로 저장할 값
    for i in range(left,right+1): # left ~ right
        cnt = 0
        for j in range(1,i+1): # i의 약수의 갯수 cnt를 구한다
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0 : # 약수의 갯수가 짝수인 경우 더하고
            ans += i
        else: # 홀수인 경우 빼준다.
            ans -= i
    return ans