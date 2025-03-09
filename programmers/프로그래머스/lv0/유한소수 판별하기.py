# 유한소수 판별하기
def solution(a, b):
    def my_func(x):
        res = []
        for i in range(2,x+1):
            while x % i == 0:
                res.append(i)
                x = x // i
        return res
    
    bunmo = my_func(b)
    
    for i in my_func(a):
        if i in bunmo:
            bunmo.remove(i)
        
    tmp = set(bunmo)
    
    if tmp == set([2]) or tmp == set([5]) or tmp == set((2,5)) or not tmp:
        return 1
    else:
        return 2
# 최대공약수 사용
# from math import gcd
# def solution(a, b):
#     b //= gcd(a,b)
#     while b%2==0:
#         b//=2
#     while b%5==0:
#         b//=5
#     return 1 if b==1 else 2

# 기약분수 알고리즘
# def solution(a, b):
#     answer = 0
#     for i in range(2, min([a, b]) + 1):
#         while a % i == 0 and b % i == 0:
#             a = a // i
#             b = b // i
#     while b % 2 == 0:
#         b = b // 2
#     while b % 5 == 0:
#         b = b // 5
#     if b == 1:
#         answer = 1
#     else:
#         answer = 2
#     return answer