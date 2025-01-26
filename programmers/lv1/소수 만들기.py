def solution(nums):
    num_of_case = []
    sosu_x = []
    
    for idx1,v1 in enumerate(nums[:-2]):
        for idx2,v2 in enumerate(nums[idx1+1:-1]):
            for v3 in nums[idx1+1+idx2+1:]:
                tmp = v1 + v2 + v3
                num_of_case.append(tmp)
                for l in range(2,int(tmp**(0.5))+1):
                    if tmp % l == 0: #소수가 아님
                        sosu_x.append(tmp)
                        break
                        
    return len(num_of_case) - len(sosu_x)

# 콤비네이션 활용
# def solution(nums):
#     from itertools import combinations as cb
#     answer = 0
#     for a in cb(nums, 3):
#         cand = sum(a)
#         for j in range(2, cand):
#             if cand%j==0:
#                 break
#         else:
#             answer += 1
#     return answer