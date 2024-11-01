# 송용진
def solution(price, money, count):
    cnt = 0
    
    # 놀이기구를 탈 때 마다 횟수를 체크하고 돈을 소진하는 for문
    for _ in range(count):
        cnt += 1
        money = money - price * cnt
    
    return 0 if money >= 0 else -money