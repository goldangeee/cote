import math

def solution(answers):
    answer = []
    
    len_a = len(answers)
    
    pattern1,len1 = '12345',5
    pattern2,len2 = '21232425',8
    pattern3,len3 = '3311224455',10
    
    p1 = pattern1 * math.ceil(len_a/len1)
    p2 = pattern2 * math.ceil(len_a/len2)
    p3 = pattern3 * math.ceil(len_a/len3)
    
    ans_cnt = [0,0,0]
    
    for i in range(len_a):
        a = str(answers[i])
        if a == p1[i]:
            ans_cnt[0] += 1
        if a == p2[i]:
            ans_cnt[1] += 1
        if a == p3[i]:
            ans_cnt[2] += 1

    m = max(ans_cnt)
    for idx,a in enumerate(ans_cnt):
        if a >= m:
            answer.append(idx+1)
    answer.sort()
    return answer
# import math

# def solution(answers):
#     supo1 = [1,2,3,4,5]
#     supo2 = [2,1,2,3,2,4,2,5]
#     supo3 = [3,3,1,1,2,2,4,4,5,5]
    
#     score1,score2,score3 = 0,0,0
    
#     length_of_answer = len(answers)
    
#     for s in supo1,supo2,supo3:
#         if length_of_answer > len(s):
#             s *= math.ceil(length_of_answer / len(s))
    
#     for i,a in enumerate(answers):          
#         if a == supo1[i]:
#             score1 += 1
#         if a == supo2[i]:
#             score2 += 1
#         if a == supo3[i]:
#             score3 += 1
            
#     score_board = (score1,score2,score3)
#     highest_score = max(score_board)
    
#     if score_board.count(highest_score) == 1:
#         return [score_board.index(highest_score)+1]
#     elif score_board.count(highest_score) > 1:
#         tmp = []
#         for i,v in enumerate(score_board):
#             if v == highest_score:
#                 tmp.append(i+1)
#         return tmp