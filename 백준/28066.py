from collections import deque

def del_sec(D):
    for _ in range(K-1):
        if len(D) == 1:
            break
        if len(D) >= 2:
            del D[1]
    return D

N,K = map(int,input().split(" "))

D = deque([i+1 for i in range(N)])

while len(D) > 1:
    D = del_sec(D)
    
    if len(D) >= 2:
        D.rotate(-1)

print(D[0])