# print문 추가 강의

# 3가지 Format Practices

x = 50
y = 100
text = 308276567
n = 'Lee'

# 출력 1 : %
ex1 = 'n = %s, s= %s, sum=%d' % (n, text, (x + y))

# n = lee , s = 3.08276567, sum = 150
print(ex1)

# 출력2 : .format
ex2 = 'n = {n}, s = {s}, sum={sum}'.format(n=n, s=text, sum=(x + y))
print(ex2)

#위 두가지는 출력 결과가 같음.

# 출력3 : f''
# 변수를 선언해도 되고 프린트문안에 직접 입력 해도 된다!
ex3 = f'n = {n}, s = {text}, sum ={x + y}'
print(ex3)
print(f'n = {n}, s = {text}, sum ={x + y}')

# 질문 ~! 구문기호

# 단위별로 표현 , 만 넣어주면 됨
m = 10000000
print(f'm: {m:,}')

print()
print()

# 정렬 !
# ^ : 가운데 정렬, < : 왼쪽 정렬 , > : 오른쪽 정렬
t = 20
# t:10 = 10자리 확보
print(f't : {t:10}')
# 가운데 정렬
print(f't center : {t:^10}')
# 왼쪽 정렬
print(f't center : {t:<10}')
# 오른쪽 정렬
print(f't center : {t:>10}')

print()
print()
# t: - < 공백은 - 로 출력 
print(f't center : {t:-^10}')
print(f't : {t:#^10}')