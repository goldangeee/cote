# 송용진
def solution(brown, yellow):
    total = brown + yellow # total은 카펫의 총 면적
    # h는 세로
    for h in range(3, total // 3 + 1): # 세로의 최솟값은 3, 최댓값은 total // 3
        if total % h == 0: # h가 조건을 만족하는지 체크
		        # w는 가로      
            w = total / h # h로 w를 구한다
            if (w-2) * (h-2) == yellow: # 노란격자의 조건을 만족하는지 체크한다
                return [w,h]