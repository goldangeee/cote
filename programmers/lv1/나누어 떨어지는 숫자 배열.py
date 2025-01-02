# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    return sorted(answer) if answer else [-1]

# def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]