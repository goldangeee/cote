# 보류(시간 초과 해결하기,성공한 스테이지 구하는 방법을 조금 더 효율적을 바꾸는 방법?)
# def solution(N, stages):
#     A = [] # 클리어 X
#     B = [] # 클리어 O # 도달 = A + B
#     clear_list = []
#     failure_rate = []
    
#     for i in range(1,N+1):
#         num = stages.count(i)
#         A.append(num)
        
#         clear_list.extend(list(range(i)) * num)
    
#     clear_list.extend(list(range(i)) * stages.count(N+1))
    
#     for j in range(1,N+1):
#         B.append(clear_list.count(j))
#         if A[j-1] + B[j-1] == 0:
#             failure_rate.append(0.0)
#         else:
#             failure_rate.append(A[j-1]/(A[j-1] + B[j-1]))
            
#     my_dict = {}
#     for idx,v in enumerate(failure_rate):
#         my_dict[idx+1] = v
#     print(my_dict)
#     return [i[0] for i in sorted(my_dict.items(),key=lambda x:(x[1],-x[0]),reverse=True)]  
            
    
    
    
        
        
        
        
        