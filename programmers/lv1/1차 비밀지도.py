# 송용진
def solution(n, arr1, arr2):

		# step1 : 두 배열을 비교해서 0,1로 구성된 tmp 배열을 만든다.
    tmp = [[0 for _ in range(n)] for _ in range(n)]# 성분이 모두 0인 n x n 행렬
    for i in range(n):
        for j in range(n):
            real_binary_of_arr1 = ('0'*(n+2-len(bin(arr1[i]))) + bin(arr1[i])[2:])
            real_binary_of_arr2 = ('0'*(n+2-len(bin(arr2[i]))) + bin(arr2[i])[2:])
            if int(real_binary_of_arr1[j]) or int(real_binary_of_arr2[j]):
                tmp[i][j] = 1
                
    # step2 : tmp를 바탕으로 0->공백 , 1->#로 바꾼 ans를 만든다.            
    ans = ['' for _ in range(n)]# 길이가 n인 문자열 자료형            
    for i in range(n):
        for v in tmp[i]:
            if v == 1:
                ans[i] += '#'
            else:
                ans[i] += ' '
    return ans       
    