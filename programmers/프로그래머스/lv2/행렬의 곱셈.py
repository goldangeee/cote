# 송용진
def solution(arr1, arr2):
    # 결과 행렬의 크기 계산
    rows_A = len(arr1)      # arr1의 행 수
    cols_A = len(arr1[0])   # arr1의 열 수
    rows_B = len(arr2)      # arr2의 행 수
    cols_B = len(arr2[0])   # arr2의 열 수

    # 결과 행렬 초기화
    ans = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # 행렬 곱셈 수행
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # arr1의 열 수이자 arr2의 행 수
                ans[i][j] += arr1[i][k] * arr2[k][j]

    return ans