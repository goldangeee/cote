# 정수가 담긴 리스트 num_list가 주어질 때,
# 모든 원소들의 곱이
# 모든 원소들의 합의 제곱보다 작으면 1을
# 크면 0을 return하도록 solution 함수를 완성해주세요.

# 내 코드

def solution(num_list):
    answer = 0
    
    mul = 1
    for i in num_list:
        mul *= i
    
    if mul < sum(num_list)**2:
        answer = 1
    else:
        answer = 0       
        
    return answer
# 예시 코드

# def solution(num_list):
#     s=sum(num_list)**2
#     m=eval('*'.join([str(n) for n in num_list]))
#     return 1 if s>m else 0