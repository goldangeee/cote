# 송용진
def solution(n): # n -> 118372
    tmp = [int(x) for x in list(str(n))]
    '''
		str(n) -> "118372"
		list(str(n)) -> ['1','1','8','3','7','2'] 
		tmp -> [1,1,8,3,7,2]
		'''
    tmp.sort(reverse=True) # tmp -> [8,7,3,2,1,1]
    tmp = [str(y) for y in tmp]# tmp -> ['8','7','3','2','1','1']
    return int(''.join(tmp))
    '''
    ''.join(tmp) ->'873211'
    '''