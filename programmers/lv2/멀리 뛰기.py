# 송용진
def solution(n):
		# 팩토리얼을 구하는 함수
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
		# 조합을 구하는 함수
    def combination(n, k):
        return factorial(n) // (factorial(k) * factorial(n - k))
    # 핵심은 2칸 뛰기를 몇 번, 어느 순서에 뛰느냐이다
    key = n // 2 # 2칸 뛰기가 최대 몇 번 가능한지
    cnt = 0 # 총 경우의 수
    if n == 1:
        return 1
    else :
		    # 2칸 뛰기 횟수에 따른 모든 경우의 수 계산( 2칸 뛰기 0번 제외)
        for i in range (1,key+1):
            cnt += combination(n - 2 * i + i,i)
        return (cnt + 1) % 1234567 # 2칸 뛰기 0번한 1가지의 경우의 수를 더해준다.
    