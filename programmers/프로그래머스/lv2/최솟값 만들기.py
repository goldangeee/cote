# 송용진
def solution(A,B):
    A.sort() # 오름차순 정렬
    B.sort(reverse=True) # 내림차순 정렬
    
    sum = 0
    for i in range(len(A)):
        sum += A[i] * B[i]
    return sum
 '''
 두 배열 곱의 합이 최소가 되려면
 A와 B의 정렬 순서가 반대가 되어야한다.
 '''