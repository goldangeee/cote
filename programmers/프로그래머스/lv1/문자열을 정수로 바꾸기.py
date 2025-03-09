#송용진
def solution(s):
    answer = 0
    
    # case1: 부호가 있는 경우
    if s[0] == '-' or s[0] == '+': 
        for i,str in enumerate(s[1:]): 
            answer += int(str) * (10 ** (len(s[1:])-(i+1))) 
            # len(s[1:])는 부호를 제외한 나머지 부분의 자릿수
            # 인덱스가 i인 부분의 숫자에는 10의 len(s[1:])-(i+1)승을 곱해줘야함
            
        # case1-2: '-'인 경우 -1을 결과값에 곱해준다.
        if s[0] == '-':
            answer = -1 * answer
            
    # case2: 부호가 없는 경우
    else: 
        for i,str in enumerate(s):
            answer += int(str) * (10 ** (len(s)-(i+1)))
            # len(s)는 자릿수
            # 인덱스가 i인 부분의 숫자에는 10의 len(s)-(i+1)승을 곱해줘야함

    return answer