# K번째수
def solution(array, commands):
    answer = []
    for c in commands:
        i,j,k = c
        answer.append(sorted(array[i-1:j-1+1])[k-1])
    return answer
'''
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
'''