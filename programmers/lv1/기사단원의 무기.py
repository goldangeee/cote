# 기사단원의 무기
def solution(number, limit, power):
    def calculate_ATK(num):
        divisor = []
        for i in range(1,int(num**(0.5)+1)):
            if num % i == 0:
                divisor.extend([i,num/i])
        return len(set(divisor))
    
    iron = 0
    for j in range(1,number+1):
        ATK = calculate_ATK(j)
        if ATK > limit:
            ATK = power
        iron += ATK

    return iron
'''
def cf(n): # 공약수 출력
    a = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            a.append(n//i)
            a.append(i)
    return len(set(a))
def solution(number, limit, power):
    return sum([cf(i) if cf(i)<=limit else power for i in range(1,number+1)])
'''

'''
리스트 컴프리헨션 방식은 메모리를 추가로 사용할 수 있으며, 
최종 결과를 리스트로 생성한 후 합계를 구하는 방식이기 때문에 
약간의 메모리 오버헤드가 있을 수 있는 단점이 있음
'''