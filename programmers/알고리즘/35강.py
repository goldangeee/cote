# # 문제 1
# # 다음과 같이 주어진 리스트를 활용하여 아래의 작업을 수행해주세요.

# nums = [7, -9, -2, 4, 3, -8, 6, 1]
# # 작업
# # 절대값 기준으로 오름차순 정렬하고 결과를 출력하세요.
# # nums.sort(key=abs)
# # print(nums) #[1, -2, 3, 4, 6, 7, -8, -9]

# # 절대값 기준으로 내림차순 정렬하고 결과를 출력하세요.
# # nums.sort(key=abs,reverse=True)
# # print(nums) #[-9, -8, 7, 6, 4, 3, -2, 1]

# # 문제 2
# # 다음과 같은 'Person' 객체 리스트를 활용하여 아래의 작업을 수행해주세요.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# people = [
# 	Person('Alice', 30),
#     Person('Bob', 35),
#     Person('Charlie', 25),
#     Person('Alice', 25),
#     Person('David', 30)
# ]
# # 작업
# # 이름으로 오름차순 정렬하고 결과를 출력하세요.
# # people.sort(key=lambda x:x.name)
# # for i in people:
# #     print(i.name, i.age)
# # 나이로 오름차순 정렬하고 결과를 출력하세요.
# # people.sort(key=lambda x:x.age)
# # for i in people:
# #     print(i.name, i.age)
# # 이름으로 오름차순 정렬 후, 같은 이름일 경우 나이가 더 많은 순으로 정렬하고 결과를 출력하세요.
# # people.sort(key=lambda x:(x.name,-x.age))
# # for i in people:
# #     print(i.name, i.age)
# # 나이로 오름차순 정렬 후, 같은 나이일 경우 이름을 알파벳 역순으로 정렬하고 결과를 출력하세요.
# # 문제 : 나이로 오름차순 정렬 후, 같은 나이일 경우 이름을 알파벳 역순으로 정렬하고 결과를 출력하세요.

# ## 먼저 이름을 기준으로 역순정렬을 한다.
# people4 = sorted(people, key = lambda person: person.name, reverse = True)
# ## 그 이후에 나이로 정렬하면, 나이가 같은 것들은 자연스럽게 원래의 순서(이름 역순)을 유지하게 된다.
# people4.sort(key = lambda person: person.age)
# print(people4)

# 문제 3
# 다음과 같은 'Student' 객체 리스트를 활용하여 아래의 작업을 수행해주세요.

# class Student:
#     def __init__(self, name, grade, score):
#         self.name = name
#         self.grade = grade
#         self.score = score
    
#     def __repr__(self):
#         return f"Student(name='{self.name}, grade='{self.grade}', score='{self.score}')"

# students = [
#     Student('Alice', 3, 85),
#     Student('Bob', 2, 90),
#     Student('Charlie', 2, 88),
#     Student('Alice', 1, 95),
#     Student('Paul', 3, 78),
#     Student('David', 3, 78)
# ]
# 작업
# 학년(grade)으로 오름차순 정렬 후, 같은 학년일 경우 점수(score)가 높은 순으로 정렬하고 결과를 출력하세요.
# students = sorted(students,key=lambda x:(x.grade,-x.score))
# print(students)
# class Student:
#     def __init__(self, name, grade, score):
#         self.name = name
#         self.grade = grade
#         self.score = score
    
#     def __repr__(self):
#         return f"Student(name='{self.name}, grade='{self.grade}', score='{self.score}')"
    
#     def __lt__(self,other):
#         if self.grade != other.grade:
#             return self.grade < other.grade
#         else:
#             return self.score > other.score

# students = [
#     Student('Alice', 3, 85),
#     Student('Bob', 2, 90),
#     Student('Charlie', 2, 88),
#     Student('Alice', 1, 95),
#     Student('Paul', 3, 78),
#     Student('David', 3, 78)
# ]

# students.sort()
# print(students)

# 점수(score)로 내림차순 정렬 후, 
# 같은 점수일 경우 이름을 알파벳 역순으로 정렬하고 결과를 출력하세요. 
# 이름까지도 같은 학생이 존재한다면 학년으로 정렬해주세요.
class Student:
    def __init__(self, name, grade, score):
        self.name = name
        self.grade = grade
        self.score = score
    
    def __repr__(self):
        return f"Student(name='{self.name}, grade='{self.grade}', score='{self.score}')"
    
    def __lt__(self,other):
        

students = [
    Student('Alice', 3, 85),
    Student('Bob', 2, 90),
    Student('Charlie', 2, 88),
    Student('Alice', 1, 95),
    Student('Paul', 3, 78),
    Student('David', 3, 78)
]

students.sort()
print(students)