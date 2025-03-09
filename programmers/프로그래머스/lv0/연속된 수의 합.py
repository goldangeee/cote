def solution(num, total):
    tmp = [i for i in range(0,num)]
    start = int((total - sum(tmp)) / num)
    return [j for j in range(start,start+num)]