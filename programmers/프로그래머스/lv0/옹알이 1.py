def solution(babbling):
    for word in "aya", "ye", "woo", "ma":
        for idx,b in enumerate(babbling):
            if word in b:
                babbling[idx] = b.replace(word,"1",1)
    cnt = 0
    for b in babbling:
        if b.isdigit():
            cnt += 1
    return cnt
        