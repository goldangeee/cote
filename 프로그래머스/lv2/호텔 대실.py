def solution(book_time):
    time_table = [0 for _ in range(60 * 24)]
    for start, end in book_time:
        start_minutes = 60 * int(start[:2]) + int(start[3:])
        end_minutes = 60 * int(end[:2]) + int(end[3:]) + 10

        if end_minutes > 60 * 24 - 1:
            end_minutes = 60 * 24 - 1

        for i in range(start_minutes, end_minutes):
            time_table[i] += 1
    return max(time_table)
'''
아이디어
1
hour과 minute으로 나눠진 시간을 minute으로 환산

2
24시간을 1분 단위로 나눠서
호텔방이 사용되는 시간을 체크하고
중복되서 사용되는 시간을 모두 카운팅해준다.
가장 카운팅이 많이된 시간대가 필요한 호텔방의 최소 갯수이다.
'''