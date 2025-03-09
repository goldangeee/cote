# 두 정수 사이의 합
def solution(a, b):
    if a > b:
        tmp = a
        a = b
        b = tmp
    answer = 0
    for i in range(a,b+1):
        answer += i
    return answer
# def adder(a, b):
#     if a > b:
#         a, b = b, a
#     return sum(range(a, b + 1))