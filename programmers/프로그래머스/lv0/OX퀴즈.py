def solution(quiz):
    ans = []
    for q in quiz:
        tmp = q.split(" = ")
        left = tmp[0]
        right = tmp[1]
        
        left_tmp = left.split(" ")
        if left_tmp[1] == "+":
            res = int(left_tmp[0]) + int(left_tmp[2])
        else:
            res = int(left_tmp[0]) - int(left_tmp[2])
        
        if res == int(right):
            ans.append("O")
        else:
            ans.append("X")
    return ans