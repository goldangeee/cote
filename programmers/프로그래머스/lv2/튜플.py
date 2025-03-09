# 송용진
def solution(s):
    answer = []    
    my_s = []
    
    s = s[2:-2] # "{{"와 ""}}"" 제거
    
    #  리스트 안에 set가 있는 my_s 만들기
    if ',' not in s:
        return [int(s)]
    else:
        for e in s.split('},{'):
            if ',' not in e:
                my_s.append(set([int(e)]))
            else:
                my_s.append( set(map( int, e.split(',') ) ))
                
        # set들의 길이 정보        
        len_list = []
        for a in my_s:
            len_list.append(len(a))
        
        # 길이가 1인 set부터 result에 들어갈 원소 추출, len_list를 이용해서 set들의 인덱스를 찾는다
        for i in range(1,len(my_s)+1):
            if i == 1: # 길이가 1인 set 자료형의 경우
                answer.append( ( my_s[len_list.index(i)] - set([]) ).pop() )
            else: # 나머지 길이의 set 자료형들은 자신보다 길이가 1 짧은 자료형과 차집합 연산을 해준다                 
                answer.append( ( my_s[len_list.index(i)] - my_s[len_list.index(i-1)] ).pop() )
        return answer
        
            
        