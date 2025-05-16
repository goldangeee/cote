# 최소직사각형
def solution(sizes):
    w,h = 0,0
    for s in sizes:
        sorted_s = sorted(s,reverse=True)
        if w < sorted_s[0]:
            w = sorted_s[0]
        if h < sorted_s[1]:
            h = sorted_s[1]
    return w*h
'''
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
'''