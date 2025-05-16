# 송용진
def solution(s):
    my_list = list(map(int,s.split(" "))) # 공백을 기준으로 나눈 객체를 int형으로 바꾸고 이를 리스트로 만든다
    return f"{min(my_list)} {max(my_list)}" # 리스트 최댓값과 리스트 최솟값