# 송용진
def solution(nums):
    return len(nums)/2 if len(set(nums)) > len(nums)/2 else len(set(nums))
    # 폰켓몬 조합의 최대 가짓수는 대부분 len(set(nums)인데
    # N/2가 len(set(nums)보다 작을때만 예외적으로 N/2가 최대 가지 수