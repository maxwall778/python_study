# 파이썬 문자형

#문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))
# len은 문자열의 길이를 알수있다.

print()
# 빈 문자열
str1_t1 = ''
str2_t2 = str()
# 빈 문자열 이기 때문에 문자열의 길이는 0 이다.
print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

print()
# 이스케이프 문자 사용
# I'm Boy
# 위와같이 ' 이런식으로 출력할때 쓰는 '' 이 들어갈경우 사용
# 특수문자 뒤에 역슬래쉬(\) 를 붙이면 '' 으로 출력해도 가능해진다.!
print("I'm Boy")
print('I\'m Boy')

# \t : 키보드의 탭키만큼 간격이 벌어짐
# \n : 문자열의 줄바꿈을 해줌
print('a \t b')
print('a \n b')

print()
escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t  Start!"
t_s2 = "New Line \n Check"

print(t_s1)
print(t_s2)

print()
# Row String 
# 앞에 소문자 r 을 붙인다! 그러면 이스케이프 문자들을 다 표시해줌!
raw_s1 = r'D:\python\test'

print(raw_s1)

print()
# 멀티라인 입력
# \ 역슬레쉬 먼저 하고 "글을적기"
multi_str = \
'''
String
Multi line
Test
'''
print(multi_str)

print()
# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3)
# 문자열에 * 를 할시 * 한 값만큼 반복
print(str_o1 + str_o2)
# 문자열 선언한 변수 + 다른 변수 시 변수값을 붙여서 프린트함
print('y' in str_o1)
# 문자열 안에 y가 str_o1 에 존재하는 지 확인
# True False 로 표시됨
print('P' not in str_o2)
# 문자열안에 p가 없는지 확인 
# True False 로 표시됨

print()
# 문자열 형 변환
# str안에 값이 들어가면 각각 int float 등 이 나오지않고
# str 값인 숫자 True 등이 들어가게 된다
print(str(66), type(str(66)))
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))

print()
# 문자열 함수(upper, isalnum, startswith, count, endswith....etc)

print("Capitalize: ", str_o1.capitalize())
# Capitalize 는 첫 글자를 대문자로 바꿔주는 문자열 함수 이다.
print("endswith?: ", str_o2.endswith("e"))
# endswith 는 마지막 글자가 () 안에 들어가는 글자인지 확인하는 함수
# True False 로 표시됨
print("replace", str_o1.replace("thon", 'Good'))
# replace 는 기존 선언되있는 문자열을 다른 문자열로 교체하여 
# 표시할수 있는 함수이다. (중요한 함수!)
print("sorted: ", sorted(str_o1))
# sorted 는 문자열을 입력받아 리스트형테로 반환해준다.
print("split: ", str_o4.split(' '))
# split 각 각의 문자열을 리스트(배열) 형태로 ()안의 문자 기준으로 
# 분리 하여 나타내줌 


print()
#반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str))
# _iter_ 가 존재시 반복을 가능하게해준다

for i in im_str:
    print(i)

print()
# 슬라이싱
str_sl = "Nice Python"

# 슬라이싱 연습
print(len(str_sl))
# 문자의 개수는 총 11개이다 (space도 문자의 개수의 포함된다)

print(str_sl[0:3])
# 0 1 2 에 관련된 것만 출력됨 즉 Nic 만 출력됨

print(str_sl[5:11])
# python 만 출력됨

print(str_sl[5:])
# 위에 프린트와 동일 하다 이유는 5: 이표시는 5부터 나머지 전부 출력이기 때문

print(str_sl[:len(str_sl)])
# str_sl[:11] 이된다 즉 처음부터 11까지 출력이도미
# len 함수를 이용하여 문자의 갯수 전체가 출력이되는것

print(str_sl[:len(str_sl)-1])
# str_sl[:10] 까지 출력됨

print(str_sl[1:9:2])
# 1 ~ 9 까지 이지만 2칸씩 보여준다 
#고로 출력물은 iePt 이다 1,3,5,7 에 해당하는 문자만 출력됨

print(str_sl[-5:])
# 오른쪽부터 5개 왼쪽으로 간 후 나머지 출력함

print(str_sl[1:-2])
# 왼쪽 1번 부터 시작하여 오른쪽끝에서 왼쪽으로 2칸 앞으로 간 곳 까지 출력
# 즉 i시작 h 끝 이됨

print(str_sl[::2])
# 처음부터 끝까지 두 칸 간격으로 출력됨

print(str_sl[::-1])
# 점프부분을 -1 를 사용하면 역으로 출력이 된다 nohtP eciN 이 출력됨

print()
# 아스키 코드 (or 유니코드)
a = 'z'

print(ord(a))
# ord 는 아스키코드 값을 찾는것
print(chr(122))
# chr은 이 숫자에 속하는 문자 값을 찾는것