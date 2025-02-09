import heapq

# heapq nlargest, nsmallest
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(heapq.nlargest(3, nums))  # 출력: [9, 6, 5]
print(heapq.nsmallest(3, nums))  # 출력: [1, 1, 2]

# 힙을 이용한 K번째 최대 원소 찾기
nums = [3, 1, 4, 1, 5, 9, 2, 6]
heap = []
k = 3
for num in nums:
    heapq.heappush(heap,num)
    if len(heap) > k:
        heapq.heappop(heap)
print(heapq.heappop(heap))

# 힙에서 가장 큰 원소 추출
nums = [3, 1, 4, 1, 5, 9, 2, 6]
heap = []
for num in nums:
    heapq.heappush(heap,-num)
print(-heapq.heappop(heap))

# 리스트를 힙으로 변환
nums = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(nums)
print(nums)

# heapq에서 가장 작은 원소 추출
nums = [3, 1, 4, 1, 5, 9, 2, 6]
heap = []
for num in nums:
    heapq.heappush(heap,num)
print(heapq.heappop(heap))

# 기본적인 heapq 사용
nums = [3,1,4,1,5,9,2,6]
heap = []
for num in nums:
    heapq.heappush(heap,num)
print(heap)