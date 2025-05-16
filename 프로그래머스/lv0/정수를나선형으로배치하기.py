# 송용진
# pattern = [(0,1),(1,0),(0,-1),(-1,0)]
# check = {(0,0):False,...,(n,n):False}

def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    answer[0][0] = 1
    cnt = 2
    loc = [0,0]
    
    while cnt <= n**2:
        while 0 <= loc[1]+1 < len(answer[loc[0]]) and answer[loc[0]][loc[1]+1] == 0:
            loc[1] += 1
            answer[loc[0]][loc[1]] = cnt
            cnt += 1      
        while 0 <= loc[0]+1 < len(answer) and answer[loc[0]+1][loc[1]] == 0:
            loc[0] += 1
            answer[loc[0]][loc[1]] = cnt
            cnt += 1
        while 0 <= loc[1]-1 < len(answer[loc[0]]) and answer[loc[0]][loc[1]-1] == 0:
            loc[1] -= 1
            answer[loc[0]][loc[1]] = cnt
            cnt += 1
        while 0 <= loc[0]-1 < len(answer) and answer[loc[0]-1][loc[1]] == 0:
            loc[0] -= 1
            answer[loc[0]][loc[1]] = cnt
            cnt += 1
    return answer