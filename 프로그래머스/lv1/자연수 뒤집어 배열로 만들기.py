def solution(n):
    return list(map(int,str(n)[::-1]))
    '''
    1. str(n) <- 자연수 n을 문자열로 만든다.
    2. [::-1] <- 이 문자열을 슬라이싱으로 뒤집는다.
    3. map(int,) <- 문자열을 모두 int형으로 객체들로 바꾼다.
    4. list() <- 객체들을 하나의 리스트 형태로 바꾼다.
    '''