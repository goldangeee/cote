def solution(arr, queries):
    answer = []
    for query in queries:
        tmp = []
        for i in range(query[0],query[1]+1):
            if arr[i] > query[2]:
                tmp.append(arr[i])
        if tmp:
            answer.append(min(tmp))
        else:
            answer.append(-1)
    return answer