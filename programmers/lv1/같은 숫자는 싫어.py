# 송용진
# idea : 인접하는 인덱스가 같으면 최종 인덱스만 남기는 방식
def solution(arr):
    ans = []
    for i in range(len(arr)):
        if i+1 <= len(arr)-1:
            if arr[i] == arr[i+1]:
                continue
            else:
                ans.append(arr[i])
        else:
            ans.append(arr[i])
    return ans