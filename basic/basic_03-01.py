# chapter 03 : 숫자형

# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀸스)
set : 집합
dict : 사전
"""

# 데이터 타입
str1 = "Python"
bool = True
str2 = 'Anaconda'
float_ = 10.0 # 10 == 10.0
int_ = 7
list = [str1, str2]
dict = {
    "name": "Machine Learning",
    "version": 2.0
}
tuple = (7, 8, 9)
set = {7, 8, 9}

# 데이터 타입 출력
print(type(str1))
print(type(str2))
print(type(bool))
print(type(float_))
print(type(int_))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))

print()

# 숫자형 연산자
"""
+
-
*
/
// : 나눈후 몫 
% : 나눈후 나머지
abs(x) : 절댓값
pow(x, y) == x의 y 제곱 == x ** y -> 2 ** 3
"""

# 정수 선언
i = 77
i2 = -14
big_int = 777777777777777777777777777777788888888888888888

#정수 출력
print(i)
print(i2)
print(big_int)

print()
# 실수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

print(f)
print(f2)
print(f3)
print(f4)

print()
# 연산 실습
i1 = 39
i2 = 939
big_int1 = 7777777777777777788888888888889
big_int2 = 3214215532645423234
f1 = 1.234
f2 = 3.939

# + 더하기
print(">>>>>>> +")
print("i1 + i2 : ", i1 + i2)
print("i1 + f2 : ", f1 + f2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)

print()
# *
print("i1 * i2 : ", i1 * i2)

print()
# 형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d))

print()
#형 변환
print(float(b))
print(int(c))
print(int(d))
print(int(True)) # True 는 1의미, False 는 0 의미
print(float(False))
print(complex(3))
print(complex('3'))  # complex 는 문자형을 -> 숫자형으로 자동변환해서 보여줌
print(complex(False))

print()
# 수치 연산 함수
print(abs(-7))

# 100을 8로 나누고 x는 몫 나머지는 y 로 변수값 할당
x, y = divmod(100, 8)

print(x + y)
# 5의 세 제곱 의미
print(pow(5,3), 5 ** 3)

# 외부 모듈 (패키지 안에 들어있다! 나중 설명)
import math

print(math.pi)
print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수
