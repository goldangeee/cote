import copy

def solution(board):
    mine_area = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
    res = copy.deepcopy(board)
    
    for i,b in enumerate(board):
        for j,c in enumerate(b):
            if c == 1:
                for m in mine_area:
                    if (i + m[0] >= 0 and i + m[0] <= len(board)-1) and (j + m[1] >= 0 and j + m[1] <= len(board)-1):
                        res[i + m[0]][j + m[1]] = 1
    tmp = 0
    for r in res:
        tmp += sum(r)
    
    return len(board) ** 2 - tmp
        
                    
                        