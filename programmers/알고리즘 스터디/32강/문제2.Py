# 다음과 같은 튜플 리스트를 활용하여 아래의 작업을 수행해주세요.

tuple_list = [
	('apple', 3),
    ('banana', 2),
    ('cherry', 1),
    ('apple', 4),
    ('banana', 1)
]
# 작업
# 첫 번째 요소 (과일 이름)를 기준으로 오름차순으로 정렬하고 결과를 출력하세요.
tuple_list.sort(key=lambda x : x[0])
print(tuple_list)
# tuple_list.sort() #첫번째 요소를 기준으로 정렬하고 그 다음은 두번째요소로 정렬
# print(tuple_list)
# 두 번째 요소 (숫자)를 기준으로 오름차순으로 정렬하고 결과를 출력하세요.
# tuple_list.sort(key=lambda x : x[1])
# print(tuple_list)