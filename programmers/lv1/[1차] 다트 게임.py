def solution(dartResult):
    points = [0] * 3
    
    dartRound = 1
    while dartRound <= 3:
        target_idx = 0
        # 점수 파트
        if dartResult[1] == '0': # 10점인 경우
            points[dartRound-1] = 10
            target_idx = 2
        else: # 2번째 자리가 보너스인 경우
            points[dartRound-1] = int(dartResult[0])
            target_idx = 1
        # 보너스 파트
        if dartResult[target_idx] == 'S':
            pass
        elif dartResult[target_idx] == 'D':
            points[dartRound-1] **= 2  
        elif dartResult[target_idx] == 'T':
            points[dartRound-1] **= 3
        target_idx += 1
        # 옵션 파트
        if target_idx <= len(dartResult)-1: 
            if dartResult[target_idx].isdigit(): # 옵션이 없고 다음 라운드가 존재
                dartResult = dartResult[target_idx:]
            else: # 옵션이 있는 경우
                if dartResult[target_idx] == '*':
                    if dartRound == 1:
                        points[dartRound-1] *= 2
                    else:
                        points[dartRound-2] *= 2
                        points[dartRound-1] *= 2
                elif dartResult[target_idx] == '#':
                    points[dartRound-1] *= -1
                    
                if target_idx+1 <= len(dartResult)-1: # 다음 라운드가 존재할 경우에만 미리 슬라이싱
                    dartResult = dartResult[target_idx+1:]
            
        dartRound += 1
    
    return sum(points)

