# 송용진
def solution(picture, k):
    # 1단계 : 각 요소들의 길이가 k배 되도록 처리
    for i,a in enumerate(picture):
        tmp = ''
        for b in a:
            tmp += b*k
            picture[i] = tmp
    # 2단계 : 각 요소들의 갯수가 k배 되도록 처리
    tmp_list = []
    for c in picture:
        tmp_list += [c] * k
        
    return tmp_list

# 0단계의 탈을 쓴 1단계