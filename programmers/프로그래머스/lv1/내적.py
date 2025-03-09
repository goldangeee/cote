# 송용진
def solution(a, b):
    ans = 0
    for i in range(len(a)):
        ans += a[i] * b[i]
    return ans
    
# 리스트 컴프리헨션과 sum 함수 사용 방법
def solution(a, b):
    return sum([a[i]*b[i] for i in range(len(a))])
    
'''
두 방법의 시간 복잡도는 동일하고
두 번째 방법은 리스트를 새로 만들기 때문에
공간 복잡도는 첫번째 방법이 더 낮다.
'''