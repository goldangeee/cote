# 송용진
def solution(name, yearning, photo):
		# 딕셔너리로 이름과 점수를 키와 밸류로 저장
    my_dict = {}
    for i in range(len(name)):
        my_dict[name[i]] = yearning[i]
    
    # 사진 루프를 돌면서 이름이 딕셔너리에 있을 경우 점수를 더해준다.
    answer = []
    for j in photo:
        sum = 0
        for k in j:
            if k in my_dict:
                sum += my_dict[k]
        answer.append(sum)
    return answer