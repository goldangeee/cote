#재귀로 문자열 뒤집기
def reverse_string(string):
    if len(string) == 1:
        return string
    return string[-1] + reverse_string(string[:-1])
print(reverse_string("hello"))