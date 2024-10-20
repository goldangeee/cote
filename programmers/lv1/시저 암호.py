# 송용진
'''
유니코드
65 <= 대문자 <= 90
97 <= 소문자 <= 122
'''

def solution(s, n):
    tmp = list(s) # 문자열은 수정이 불가하기 때문에 리스트형 s, tmp를 만든다.
    
    for i, x in enumerate(s):        
        if x == " ":
            continue # 공백일 경우 skip하고 다음 문자로 넘어간다
        elif 65 <= ord(x) <= 90 : # 대문자일 경우
            a,b = 65,90
        else: # 나머지는 소문자일 경우 밖에 없다
            a,b = 97,122
        
        if ord(x) + n > b: # n을 더했을 때 대소문자의 유니코드 범위를 벗어났을 경우
            tmp[i] = chr((ord(x) + n) - b + a - 1) 
            # 시작 범위로 다시 돌아온 유니코드 번호에 해당하는 문자로 
            # 리스트 요소를 바꿔준다
        else:
            tmp[i] = chr(ord(x) + n) 
            # 밀려난 만큼 변경된 문자로 리스트 요소를 교체해준다.
            
    return ''.join(tmp) # 변경된 리스트를 다시 문자열로 바꿔준다.
