# 정수 리스트 num_list가 주어질 때,
# 첫 번째로 나오는 음수의 인덱스를
# return하도록 solution 함수를 완성해주세요.
# 음수가 없다면 -1을 return합니다.

# 내 코드

def solution(num_list):
    answer = -1
    list_length = len(num_list)
    
    for i in range(list_length):
        if num_list[i] < 0:
            answer = i
            break
        else:
            continue
    
    return answer
# 예시 코드

# def solution(num_list):
#     answer = -1
#     for i,val in enumerate(num_list):
#         if val<0:
#             answer = i
#             break
#     return answer