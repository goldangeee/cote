def solution(arr, k):
    answer = []
    cnt = 0
    
    for a in arr:
        if cnt >= k:
	        break
        if a not in answer:
            answer.append(a)
            cnt += 1
            
    if len(answer) < k:
        for _ in range(k-len(answer)):
            answer.append(-1)       
        
    return answer