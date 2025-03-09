# 송용진
def solution(n):
    k = 1
    while True:
        if bin(n)[3:].count("1") == bin(n+k)[3:].count("1"): # 이진수의 1의 갯수가 같은 경우
            return n+k
        else:
            k += 1 # 1씩 늘려가면서 찾는다