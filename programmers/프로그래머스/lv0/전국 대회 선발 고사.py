def solution(rank, attendance):
    tmp_list = []
    tmp_dict = {}
    
    for i in range(len(rank)):
        tmp_dict[i] = rank[i] # 번호 : 등수 형태의 딕셔너리를 만든다
        if attendance[i] == True:
            tmp_list.append(rank[i]) 
            # 참석할 수 있는 학생의 등수만 모은 tmplist를 만든다
            
    tmp_list.sort() # tmplist를 오름차순 정렬한다
    
    for key,value in tmp_dict.items():
        if value == tmp_list[0]:
            a = key  # 참석자 중 1등의 번호는 a
        elif value == tmp_list[1]: 
            b = key # 참석자 중 1등의 번호는 b
        elif value == tmp_list[2]: 
            c = key # 참석자 중 1등의 번호는 c
            
    return 10000*a + 100*b + c 
            