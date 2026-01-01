# Chapter 01 : print

# 1.print 출력 : '' ,  "", ''' ''', """ """ 등 출력시 사용할수있음.
# 자주 사용되는것은 '' 이 형태임
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

# print()시 공백 효과
print()

# 2.separator 옵션 -> sep = '' 형태로 사용 하고 각 글자사이에 무엇을 넣는지 결정!

# 기본 출력 형태
print('P', 'Y', 'T', 'H', 'O', 'N')

# (1) 공백 없이
print('P', 'Y', 'T', 'H', 'O', 'N', sep ='')

# (2) 각문자 사이에 , 
print('P', 'Y', 'T', 'H', 'O', 'N', sep =',')

# (3) 각문자 사이에 |
print('P', 'Y', 'T', 'H', 'O', 'N', sep ='|')

# (4) 각문자 사이에 공백 공백 4개
print('P', 'Y', 'T', 'H', 'O', 'N', sep ='    ')

print('010', '7777', '1234', sep= '-')

print('python', 'google.com', sep='@')

# 3. end 옵션 : 끝부분은 end로 들어가있는 문자로 처리한다

# print의 출력물을 이을수있다. 
print('welcom to', end=' ')
print('IT News', end=' ')
print('Web site')

#file 옵션

import sys
# 외부의 특정한 파일에있는 옵션을 사용할거다 의미
print('Learn Python', file=sys.stdout)
# 줄바꿈처리
print()

#format 사용(d : 3, s : 'python', f : 3.1445454)  (d = 정수 s = 문자열 f = 실수)

# 첫번째 s 에는 one 두번째 s 에는 two 가 들어가서 출력됨
# 정확함!
print('%s %s' %('one', 'two'))

# {} 이안에 뭐든 들어갈수있어 유연하게 사용가능
# 이때 !! .format 함수를 사용한다 %s 같은 지정된것은 % 를 사용하지만 
# {} 같은 뭐든 들어갈수있는 것을 사용시 .format 을 사용해준다
print('{} {}'.format('one', '2'))

# {} 안에 순서를 지정하며 사용할수있다!
print('{1} {0}'.format('one', 'two'))

#줄바꿈 처리
print()

# %s : 문자열 출력
# 10개의 자리를 확보를 하겠다란 의미  즉 nice는 4글자 6글자 공백이 들어간다.

# 오른쪽부터 nice 를 채우고 나머지를 공백으로 채운다
print('%10s' % ('nice'))

#위와 결괏값은 같다
#오른쪽부터 텍스트를 채우고 나머지를 공백처리
print('{:>10}'.format('nice'))

# 두 결과값은 같고
# 왼쪽부터 nice 를 채우고 나머지를 공백으로 채운다
print('%-10s' %('nice'))
# 기호 생략시 왼쪽에 텍스트 채운후 나머지를 공백
print('{:10}'.format('nice'))

# {: >10} : 와 >10 사이에 문자를 넣는경우 
# 나머지 공백은 추가한 문자로 채워진다.
print('{:_>10}'.format('nice'))

# ^ 를 사용시 텍스트가 중앙으로 정렬이된다.
print('{:^10}'.format('nice'))

# 앞에 . 을찍어줄시 5글자만 절삭한다.
# .을 안붙일시 내가 원하는 자리를 지정해도 전부 출력하게된다
print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
# 공간은 10개가있지만 왼쪽부터 5개만 출력한다.
print('{:10.5}'.format('pythonstudy'))

#줄바꿈 처리
print()
# %d  : 정수 출력

# 아래 두개는 동일하게 출력이 된다.
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

# 아래 두개는 같은 표현이다
print('%4d' % (42))
print('{:4d}'.format(42)) 

#줄바꿈 처리
print()
# %f : 실수 출력

# 전부 출력되진않고 소수점 6자리 까지 출력된다.
print('%f' % (3.1414144114))

# 1.18 의 의미는 정수는 1자리 소수는 18자리까지 출력해라 의미
print('{:1.18f}'.format(3.1414144114))
# 위와 동일하게 출력.
print('{:f}'.format(3.1414144114))

# 총 6자리를 선정하고 정수가 1자리 소수는 .2 이므로 2자리
# 나머지는 정수 부분에 숫자로 채움 중간에 들어가는 . 도 자리수를 차지함!
print('%06.2f' % (3.141592653589793))

#위와 동일하게 출력.
print('{:06.2f}'.format(3.141592653589793))