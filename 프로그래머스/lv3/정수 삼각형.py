import copy

def solution(triangle):
    tri_sum = copy.deepcopy(triangle)
    for i1,t in enumerate(triangle):
        if i1 == 0:
            continue
        for i2,num in enumerate(t):
            if i2 == 0:
                tri_sum[i1][i2] = tri_sum[i1-1][i2] + triangle[i1][i2]
            elif i2 == len(t)-1:
                tri_sum[i1][i2] = tri_sum[i1-1][i2-1] + triangle[i1][i2]
            else:
                tri_sum[i1][i2] = max([tri_sum[i1-1][i2-1],tri_sum[i1-1][i2]]) + triangle[i1][i2]
    return max(tri_sum[len(triangle)-1])