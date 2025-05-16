#완전탐색
from itertools import permutations as perm

def solution(k, dungeons):
    tmp = k
    my_list = []
    length = len(dungeons)
    for p in perm(range(length),length):
        cnt = 0
        k = tmp
        for j in p:
            if dungeons[j][0] <= k:
                k -= dungeons[j][1]
                cnt += 1
                if k == 0:
                    break
        my_list.append(cnt)
    return max(my_list)

#dfs로도 구현 가능