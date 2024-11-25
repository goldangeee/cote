def solution(dots):
    for a in range(len(dots)-1):# a는 0,1,2
        for b in range(a+1,len(dots)):# b는 a+1 ~ 3
            if a != b:
                tmp = [0,1,2,3]
                tmp.remove(a)
                tmp.remove(b)
                x1 = dots[a][0] - dots[b][0]
                y1 = dots[a][1] - dots[b][1]
                x2 = dots[tmp[0]][0] - dots[tmp[1]][0]
                y2 = dots[tmp[0]][1] - dots[tmp[1]][1]
                if y1 / x1 == y2 / x2:
                    return 1
    return 0