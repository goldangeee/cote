def solution(dots):
    x_arr = []
    y_arr = []
    for x,y in dots:
        x_arr.append(x)
        y_arr.append(y)
    answer = (max(x_arr)-min(x_arr))*(max(y_arr)-min(y_arr))
    return answer