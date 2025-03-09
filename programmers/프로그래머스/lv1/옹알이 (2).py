def solution(babbling):
    babbling_possible = [True] * len(babbling)
    nephew = ["aya", "ye", "woo", "ma"]
    for idx,b in enumerate(babbling):
        for n in nephew:
            if babbling_possible[idx]:
                if n * 2 in b:
                    babbling_possible[idx] = False
                    break
        if babbling_possible[idx]:
            for n2 in nephew:
                if b.isdigit():
                    break
                b = "0".join(b.split(n2))
            if not b.isdigit():
                babbling_possible[idx] = False

    return babbling_possible.count(True)

# def solution(babbling):
#     answer = 0
#     for i in babbling:
#         for j in ['aya','ye','woo','ma']:
#             if j*2 not in i:
#                 i=i.replace(j,' ')
#         if len(i.strip())==0:
#             answer +=1
#     return answer

# 1. 숫자로 바꾼 다음에 isdigit을 사용하는 방식
# 2. 공백으로 바꾼 뒤 strip과 len을 사용하는 방식

# 불리언 리스트를 따로 만들지 않고도
# 발음할 수 있는 것들을 세는 것만으로도 구현 가능