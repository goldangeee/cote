def solution(n):
    ans = 0
    for j in range(2,n+1): # 1은 소수가 아니기 때문에 2부터 시작
        for i in range(2,int(j**(0.5)+1)):# 1과 자신을 제외한 약수가 있는지 확인할 범위
            if j % i == 0:# 1과 자신 이외의 약수가 존재할 경우
                ans += 1# 소수가 아닌 수의 갯수를 늘려준다
                break# 반복문을 나간다
    return (n-1) - ans # (전체 - "1") - 소수가 아닌 수 = 소수의 갯수