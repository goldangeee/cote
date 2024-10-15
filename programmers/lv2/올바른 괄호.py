def solution(s):
    # 1차 필터링 
  if s[0] == ')' or s[-1] == '(' or len(s) % 2 != 0 or s.count('(') != s.count(')') : #시작이 ')' / 끝이 '(' / 길이가 2의 배수가 아닌 경우 / '('와 ')'의 갯수가 다를 경우
	  return False
  else: # 2차 필터링 (1차에서 필터링 되지 않은 false를 찾는 과정)
	  s = s.replace('()','') # '()' 형태를 다 소거
	  
	  if s == '': # 모두 소거된 경우 true
	      return True
	  else: # 모두 소거되지 않았을 경우
	      if s[0] == ')' or s[-1] == '(': 
	          return False # 소거되고 남은 부분의 시작이 ')' / 끝이 '('인 경우 false
	      else:
	          return True
