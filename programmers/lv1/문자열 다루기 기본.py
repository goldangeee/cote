# 문자열 다루기 기본
def solution(s):
    L = len(s)
    return (L==4 or L==6) and s.isdigit()

'''
def alpha_string46(s):
    return s.isdigit() and len(s) in [4,6]
'''