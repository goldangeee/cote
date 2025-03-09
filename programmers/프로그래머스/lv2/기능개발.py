# 송용진
from collections import deque
def solution(progresses, speeds):
    ans = []
    progresses_queue = deque(progresses)
    speeds_queue = deque(speeds)
    
    while len(progresses_queue) > 0:
		    # 각 작업의 진행률 업데이트
        for i in range(len(progresses_queue)):
            if progresses_queue[i] < 100:
                progresses_queue[i] += speeds_queue[i]

        done = 0
        while progresses_queue[0] >= 100:
            progresses_queue.popleft()
            speeds_queue.popleft()
            done += 1
            if len(progresses_queue) == 0:
                break

        if done >= 1:    
            ans.append(done)
    
    return ans