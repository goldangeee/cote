def binary_search(arr, low, high, x):
    if high >= low: # 조건 간과 주의!
        mid = (high + low) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    
    return -1


# 정렬된 리스트와 찾고자 하는 값을 설정합니다.
nums = [2, 3, 4, 10, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 700, 800, 1000, 1115]
x = 800

# 이진 탐색 함수를 실행합니다.
result = binary_search(nums, 0, len(nums)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")