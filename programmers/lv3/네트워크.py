from collections import deque

def find_my_net(com,visited,computers):
    queue = deque([com])
    while queue:
        target = queue.popleft()
        if visited[target] is False:
            visited[target] = True
            for idx,v in enumerate(computers[target]):
                if target == idx:
                    continue
                if v == 1:
                    queue.append(idx)
        
    

def solution(n, computers):
    net_cnt = 0
    
    visited = [ False for _ in range(n)]
    
    for com in range(n):
        if visited[com] is False:
            net_cnt += 1
            find_my_net(com,visited,computers)
            
    
    
    
    return net_cnt