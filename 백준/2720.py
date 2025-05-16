# 5/11 송
T = int(input())

values = [25,10,5,1]

for _ in range(T):
    change = int(input())
    ans_str = ''
    for idx,value in enumerate(values):
        ans_str += str(change // value) + ' '
        change = change % value
    print(ans_str[:-1])