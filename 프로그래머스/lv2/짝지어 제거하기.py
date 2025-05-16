# 송용진
def solution(s):
    def del_pair(x):
        stack = []
        for char in x:
            if stack and stack[-1] == char:
                stack.pop()  # 짝이 맞으면 스택에서 제거
            else:
                stack.append(char)  # 짝이 아니면 스택에 추가
        return stack  # 남은 요소들 반환

    tmp = list(s)

    return 1 if not del_pair(tmp) else 0  # 남은 요소가 없으면 1 반환