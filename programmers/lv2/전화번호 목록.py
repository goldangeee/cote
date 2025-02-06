def solution(phone_book):
    phone_book.sort()  # 전화번호를 사전순으로 정렬
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False  # 접두사 관계가 있을 경우
    return True  # 접두사 관계가 없을 경우

# 해쉬(딕셔너리) 사용
# def solution(phone_book):
#     answer = True
#     hash_map = {}
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1
#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
#             if temp in hash_map and temp != phone_number:
#                 answer = False
#     return answer
'''
temp가 해시맵에 존재하는지 확인
만약 temp가 해시맵에 있고, 
temp가 현재 전화번호와 다르다면, 
이는 현재 전화번호가 다른 전화번호의 접두사임을 의미
'''