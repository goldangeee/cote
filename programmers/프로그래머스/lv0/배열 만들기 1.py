def solution(n, k):
    tmp = [x for x in range(1,n+1) if x % k == 0]     
    tmp.sort()
    return tmp