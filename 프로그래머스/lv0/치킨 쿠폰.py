def solution(chicken):
    coupon = 0
    service_chicken = 0
    while chicken:
        chicken -= 1
        coupon += 1
        if coupon == 10:
            coupon -= 10
            service_chicken += 1
            coupon += 1
    return service_chicken