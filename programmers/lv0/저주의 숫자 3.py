def solution(n):
    ans = []
    real_num = 1
    
    while len(ans) != n:
        if real_num % 3 != 0 and '3' not in str(real_num):
            ans.append(real_num)
        real_num += 1
    
    return ans[n-1]