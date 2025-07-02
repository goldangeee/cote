def solution(s, skip, index):
    # print(ord('a'))
    # print(ord('z'))
    result = ''
    for x in s:
        word_num = ord(x)
        for _ in range(index):
            word_num += 1
            if word_num >= 123:
                word_num = word_num % 123 + 97
            while chr(word_num) in skip:
                word_num += 1
                if word_num >= 123:
                    word_num = word_num % 123 + 97
        result += chr(word_num)
    return result