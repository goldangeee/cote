# 송용진
def solution(s):
    ans = ''
    for word in s.split(' '): # s.split(' ')는 공백을 기준으로 나눈 객체
        for i,w in enumerate(word):
            if i % 2 == 0:
                ans += w.upper()
            else:
                ans += w.lower()
        ans += " "
    return ans[:-1]