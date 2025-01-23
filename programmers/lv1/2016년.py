def solution(a, b):
    month = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    tmp = 0
    if a == 1: # a가 1월인 경우
        tmp = b-a
    else:
        tmp += 30 # 1월 31일까지 일 수 계산
        for i in range(2,a): # 2월부터 a월 전까지는 통째로 계산
            tmp += month[i]
        tmp += b # a월의 일 수만 계산
    return day[tmp % 7]

'''
def getDayName(a,b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return day[(sum(month[:a-1])+b-1)%7]
'''

'''
month[:a-1])+b-1로 1월까지 커버할 수 있는 좋은 아이디어
'''