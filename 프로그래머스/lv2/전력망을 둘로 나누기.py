import copy

def solution(n, wires):
    answers = []
    #끊을 전력망 "target" 선정하기
    for i in range(len(wires)):
        target = wires[i]
        copy_wires = copy.deepcopy(wires) #매 루프마다 원본을 복사해서 사용해서 원본을 보존
        copy_wires.remove(target)# 끊을 전력망이 정해졌다면 복사본에서 끊어진 전력망의 정보를 제거
        # 끊어진 전력망을 기준으로 pg1과 pg2로 나누기
        pg1 = [target[0]]
        pg2 = [target[1]]
        
        while copy_wires: # 연결 정보로 전력망 분류가 끝날때가지 루프를 돌면서 송전탑을 분류
            for c in copy_wires[0]:
                if c in pg1:
                    pg1.extend(copy_wires[0])
                    copy_wires.pop(0)
                    break
                elif c in pg2:
                    pg2.extend(copy_wires[0])
                    copy_wires.pop(0)
                    break
            else: # 현재 정보로 알아낼 수 없을 경우 분류 마지막으로 미룬다.
                copy_wires.append(copy_wires.pop(0))
        # 송전탑 중복 제거        
        pg1 = set(pg1)
        pg2 = set(pg2)
        # pg1과 pg2의 차이 구하기
        if pg1 & pg2: # 두 전력망에 겹치는 송전탑이 있을 경우 전력망이 제대로 끊어진 것이 아니므로 제외
            pass
        else:
            answers.append(abs(len(pg1) - len(pg2)))
        
    return min(answers)
 