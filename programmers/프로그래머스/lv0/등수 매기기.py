def solution(score):
    avg = []
    for s in score:
        avg.append((s[0]+s[1]) / 2)
    ans = []
    sorted_avg = sorted(avg,reverse=True)
    for a in avg:
        ans.append(sorted_avg.index(a)+1)
    return ans