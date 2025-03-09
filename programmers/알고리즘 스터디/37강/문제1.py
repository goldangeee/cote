import heapq

nums = [15, 22, 7, -8, 33, 12, 42, -3, 18, 29, -11]
# 작업
# heapq 모듈을 활용하여 nums 리스트를 최소 힙으로 변환하고 결과를 출력하세요.
heapq.heapify(nums)
# print(nums)

# 최소 힙에서 가장 작은 원소를 추출하고, 그 후의 힙의 상태를 출력하세요.
# heapq.heappop(nums)
# print(nums)
# 변환한 힙에서 가장 큰 원소를 추출하고, 그 후의 힙의 상태를 출력하세요.
new_nums = [-i for i in nums]
heapq.heapify(new_nums)
heapq.heappop(new_nums)
new_nums = [-i for i in nums]
print(new_nums)