list1 = [2, 7, 9, 2, 4, 3, 8, 6, 1]
# 오름차순으로 정렬하고 결과를 출력하세요.
print(sorted(list1))
# 내림차순으로 정렬하고 결과를 출력하세요.
print(sorted(list1,reverse=True))
# 중복된 숫자를 제거한 후 오름차순으로 정렬하고 결과를 출력하세요.
list1 = sorted(set(list1))
print(list1)
# print(sorted(list(set(list1))))
'''
set 자료형은 본질적으로 정렬된 구조가 아니지만, 
sorted() 함수는 입력으로 받은 iterable(반복 가능한 객체)을 정렬하여 리스트로 반환
'''