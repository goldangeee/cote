def solution(k, m, score):
    score.sort(reverse=True)
    ans = 0
    for i in range(len(score)//m):
        ans += min(score[0+i*m:i*m+m])*m
    return ans
# def solution(k, m, score):
#     score.sort(reverse=True)
#     return sum(min(score[0+i*m:i*m+m])*m for i in range (len(score)//m))