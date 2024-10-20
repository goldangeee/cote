# 송용진
def solution(s):
    answer = ''
    for a in s.split(' '):
        if a == '':
            answer += a + ' '            
        elif not a[0].isdigit() or 97 <= ord(a[0]) <= 122:
            answer += a[0].upper() + a[1:].lower() + ' '
        else:
            answer +=  a[0] + a[1:].lower() + ' '
    return answer[:-1]