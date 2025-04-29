# 파이썬은 위에서 아래로 읽힌다
# 변수는 변하는 수 #변수에는 변수 작성방법이 있다 제약조건이 있다 
# #숫자로 시작하면안되고, 
# 예약어도안됨 앞자리 대문자 소문자 구분
# 상수는 파이썬에서 지원안한다 전체대문자로 입력
# 자바는 상수가 있다
# 변수의 타입은 
# a = "good" < 문자타입
# type(a) >출력안됨
# print 앞에 입력해야 출력이된다

#정수 >양의정수 음의정수 0

a = 10
b = 20
c = 0
d = -40

print(type(a),type(b),type(c),type(d))
# print(int(9.33333))<< 9로 출력

# 실수
number1 = 3.12
number2 = -0.12
print(type(number1),type(number2))

# fioat()< 형이라고 함
# print(float(3))<< 3은 정수인데. 3을 .0을 붙이면서 float형태로 바꿔 출력

# 무한대(인피니티) 파이썬에서 무한대를 표시하는 방법
# x = float("inf") 
# y = float("-inf")
# char a = 'a' < 파이썬에서는 작은따옴표는 쌍따옴표랑 같은 문자열이다
# str1 = "abcd"
# str2 = 'abcd' 둘다 같은 문자열
# '''<<작은 따옴표안에있는건(무한대로) 모두 주석처리가 된다
str3 = '''
오늘은 4월 28일 입니다.
5월이 멀지 않았네요.
'''
print(type(str3))
print(str3)

str4 = '''
내일 날씨는 화창 할 겁니다.
즐거운 주말 보내세요.
'''
print(type(str4))
print(str4)

# str에 ''' 담으면 띄어쓰기까지도 모든걸 문자열로 인식한다 

str4 = '오늘은 4월 28일입니다.\n\n5월이 멀지 않았네요.'
# 줄바꿈할때는 '''<이방법이 더 편하다,  \n 붙여쓰기가능하다

print(str3+str4)

# 문자열 이어붙이기

str6 = "modu"
str7 = "labs"

# 첫번째 방법, 이어붙이는 방법의 기준은 str6이 된다. 기준은 바뀌면 안된다.
print(str6+str7)
str8 = str6+str7

# 두번째 방법
print(str8)

# 개인정보 출력해보기
# 1. 성, 이름 변수를 따로 만들어서 + 로 합친 후 출력
# 2. 주민등록번호도 1번과 같이
# 3. 이메일 {아이디} {@} {네이버, 구글}

str9 = "홍"
str10 = "길동"
print(str9+str10)
str11 = str9+str10

str12 = "123456"
str13 = "-5678910"
print(str12+str13)
str14 = str12+str13

str15 = "abcd"
str16 = "@"
str17 = "naver.com"
print(str15+str16+str17)
str18 = str15+str16+str17

print(str11)
print(str14)
print(str18)

# 문자열 반복하기

str10 = str10 * 10

test2 = "30"

print(str10)

print(str10 * test2)





