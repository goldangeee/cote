# 크기가 작은 부분 문자열
def solution(t, p):
    answer = 0
    
    p_len = len(p)
    real_p = int(p)
    last_idx = (len(t)-1) - (len(p)-1)
    
    for i in range(0,last_idx+1):
        if int(t[i:i+p_len]) <= real_p:
            answer += 1
            
    return answer