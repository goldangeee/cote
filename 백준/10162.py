# 5/14 송
T = int(input())
button = [300,60,10]
ans = []
for b in button:
    ans.append(T // b)
    T %= b
if T != 0:
    print(-1)
else:
    for a in ans:
        print(a,end=" ")