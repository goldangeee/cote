# 송용진
def solution(food):
		# idea : 결과물은 A + "0" + A[::-1] 구조
    
    # 문자열 A를 만들어준다.
    A = ''
    for i,x in enumerate(food[1:]):
        A += str(i+1) * int(x//2)
        
    return A + '0' + A[::-1]
