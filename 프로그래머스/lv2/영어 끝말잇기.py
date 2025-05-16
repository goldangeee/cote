# 송용진
def solution(n, words):
    answer = []
    cnt = [0] * n # 탈락자가 발생할 때 까지 자신의 차례가 몇 번 왔는지 체크
    for i,v in enumerate(words):
        if i == 0: # 끝말잇기의 첫 단어
            cnt[0] += 1 # 차례가 온 횟수를 늘려준다.
        else:
            cnt[i%n] += 1 # 차례가 온 횟수를 늘려준다 / i%n인 이유는 n을 주기로 반복되기 때문
            # 끝말이 이어지는지 and 이미 나온 정답인지
            if words[i-1][-1] == words[i][0] and v not in words[:i]:
                continue
            else:
                return [i%n+1,cnt[i%n]]# i%n+1인 이유는 실제 번호는 인덱스와 달리 0부터 시작이 아닌 1부터 시작이기 때문
    return [0,0]            
