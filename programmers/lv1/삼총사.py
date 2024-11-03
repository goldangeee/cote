# 송용진
def solution(number):
    cnt = 0 # 삼총사의 총 경우의 수
    for i1,v1 in enumerate(number[:-2]): # 첫 번째 멤버, -2 인덱스 전까지인 이유는 나머지 멤버 2명을 남기기 위함
        for i2,v2 in enumerate(number[(i1)+1:-1]):# 두 번째 멤버의 범위는 첫번째 멤버의 인덱스 다음부터 시작, -1 인덱스 전까지인 이유는 나머지 멤버 1명을 남기기 위함
            for v3 in number[(i1+1+i2)+1:]:# 세 번째 멤버, (i1+1+i2)는 두 번째 멤버의 인덱스
                if v1+v2+v3 == 0:
                    cnt += 1
    return cnt