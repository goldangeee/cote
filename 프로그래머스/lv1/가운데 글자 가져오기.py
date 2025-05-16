# 송용진
def solution(s):
    if len(s) % 2 == 0: # 길이가 짝수일 경우
        return s[0+int(len(s)/2)-1] + s[0+int(len(s)/2)]
    else: # 길이가 홀수일 경우
        return s[0+int(len(s)/2)]