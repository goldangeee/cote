def solution(priorities, location):
    order = [0] * len(priorities)
    p = []
    for idx,v in enumerate(priorities):
        p.append((idx,v))

    cnt = 1
    while p:
        target = p.pop(0)
        tmp = [i[1] for i in p]
        if p and max(tmp) > target[1]:
            p.append(target)
        else:
            order[target[0]] = cnt
            cnt += 1
    return order[location]