# 송용진
def solution(num):
    cnt = 0 # 작업 반복 횟수
    
    while num != 1 and cnt < 500: # 1이 될때까지 500번 이하로 반복
        if num % 2 == 0: 
            num /= 2 # 짝수면 2로 나눈다
        else: 
            num = num * 3 + 1 # 홀수면 3을 곱하고 1을 더한다
        cnt += 1 # 작업이 끝나면 작업 횟수를 1 추가해준다
    
    return cnt if num == 1 else -1 # 결과가 1이되면 반복횟수를 출력 그렇지 않으면 -1을 반환
    