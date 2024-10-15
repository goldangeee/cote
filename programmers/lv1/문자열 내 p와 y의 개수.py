# 송용진
def solution(s):
    return True if s.count("p") + s.count("P") == s.count("y") + s.count("Y") else False
    # p와 P의 갯수의 합과 y와 Y 갯수의 합이 같으면 True