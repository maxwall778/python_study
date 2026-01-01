# chapter 02 : 변수


# 기본 선언

# n 에 700의 값을 할당한다.
n = 700
print(n)
# type 은 해당 선언 변수에 타입을 알려줌.
print(type(n))

print()
# 동시 선언
x = y = z =700
print(x,y,z)

print()
# 재선언
var = 75

var = "Change Value"

print(var)
print(type(var))

print()
# Object References
# 변수 값 할당 상태 
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# ex01)
print(300)
print(int(300))


print()
# ex02)
# 자동으로 타입에 맞는 타입을 지정해서 출력해줌.
n = 777
print(n, type(n))

print()
# m = 777
m = n 
print(m, type(m))

# m 값을 재할당하여도 n 은 바뀌지않음!
m = 400
print(m, n)
print(type(m), type(n))

print()
# id(identity)확인 : 객체의 고유값 확인

m = 800
n = 655

print(id(m))
print(id(n))

print(id(m) == id(n))
print()

# 같은 값을 할당 하였기 때매 True 가 나온다.
# 파이썬이 각각의 id 를 할당해주는게 아닌 값이 같으니 id 도 같은값으로 할당해주는것
m = 800
n = 800


print(id(m))
print(id(n))

print(id(m) == id(n))
print()

# 다양한 변수 선언
# Camel Case : numberofCoLLageGraduates -> Method 선언시 사용
# Pascal Case : NumberofCoLLegeGraduates -> Class 선언시 사용
# Snake Case : number_of_coLLege_graduates

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
# 특수문자나 숫자로 시작시 사용불가! _나 $ 등을 시작
# 웬만하면 소문자 시작이나 snake case 식으로 사용하면 좋음

# 예약어는 변수명으로 불가능

# ex) for , as, class 등 예약어는 사용할수없다!