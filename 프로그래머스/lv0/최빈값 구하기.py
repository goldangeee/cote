def solution(array):
    my_set = set(array) # array의 중복제거
    value = [] # array의 값 정보
    cnt = [] # array의 특정 값의 빈도수
    
    for x in my_set:
        value.append(x) # count할 값을 일단 추가
        cnt.append(array.count(x)) # 특정 값의 빈도수 추가
        
    if cnt.count(max(cnt)) == 1: # 빈도수의 최대값이 하나일 경우
        return value[cnt.index(max(cnt))] # 빈도수의 최대값의 인덱스를 통해 해당 빈도수를 가진 값을 리턴
    else:# 빈도수의 최대값이 여러 개일 경우
        return -1