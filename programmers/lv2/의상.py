def solution(clothes):
    my_dict = {}

    # 의상의 종류별로 수를 세기
    for c in clothes:
        if c[1] in my_dict:
            my_dict[c[1]] += 1
        else:
            my_dict[c[1]] = 1

    # 각 종류의 의상 수에 1을 더한 값을 곱하고, 마지막에 1을 뺀다.
    ans = 1
    for count in my_dict.values():
        ans *= (count + 1)  # 각 종류에서 선택하지 않을 경우를 포함해 +1

    return ans - 1  # 최소 하나의 의상은 착용해야 하므로 1을 뺀다.