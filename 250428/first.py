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

str4 = '오늘은 4월 28일입니다.\n5월이 멀지 않았네요.'
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
# 문제 1 (이름출력)
str9 = "홍"
str10 = "길동"
print(str9+str10)
str11 = str9+str10

# 문제 2 (주민번호출력)
str12 = "123456"
str13 = "-5678910"
print(str12+str13)
str14 = str12+str13

# 문제 3 (이메일주소출력)
str15 = "abcd"
str16 = "@"
str17 = "naver.com"
print(str15+str16+str17)
str18 = str15+str16+str17

print(str11)
print(str14)
print(str18)

# 문자열 반복하기

str10 = str10 * 3
print(str10)

test2 = "30"
print(test2)

## 변수를 이용하여 문자를 만들기
a = "4"
b = "28"
# 기본방식
# print("오늘은 "+a+"월 "+b+"일입니다.") <활용적이지 못함
# f-string (에프스트링)
# f"{변수}" > 쌍따옴표앞에 F를붙이고 중괄호안에 변수를 넣고 식값을 넣는다. 
# 굉장히 많이 쓴다, 기억하라
print(f"오늘은 {a}월 {b}일입니다.")
print(f"오늘은 {a}월 {b*10}일 입니다.")

## 문자열인덱스 > 인덱싱 
# 인텍스 문자열 마지막 값은 -1이라고 하고, 왼쪽에서 오른쪽으로 >갈 경우 0부터
# 오른쪽에서 왼쪽으로 갈경우 -1부터 < (띄어쓰기도 포함)

s = "life is good"
print(s[0])
print(s[6])
print(s[3])
print(s[-1])
# print(s[300]) >  string index out of range > 인덱스 범위를 벗어났나고 알려줌
# 주민등록번호가 13자리
# 에러에 대한 대비코드를 사용

## 슬라이싱 > 문자열에서 필요한 문자만 추출 "life is good">[start(0):stop(3):step(생략가능)]
print(s[0:3]) 
print(s[0:4:2]) ## s[0:3:1] > 0부터 4까지 2씩 늘려라 출력값은 l(0)f(0부터 2칸뒤)가 출력된다
# stop인텍스는 슬라이싱 영역에 포함되지 않.는.다
# 0부터 4까지라고 하면3과 4사이 띄어쓰기는 생략, 3까지만생각하면 된다
# 다양한 슬라이싱 방법
s ='weniv CEO licat'
print(1, s[0:5]) # 출력 : weniv (앞에 0부터 4글자만 띄어쓰기 생략 출력
print(2, s[6:]) # 출력 : CEO licat (6글자부터 끝까지 출력)
print(3, s[:]) # 출력 : weniv CEO  (전체출력)
print(4, s[::-1]) # 출력 : tacil OEC vinew (거꾸로 출력)
print(5, s[::2]) # 출력 : wnvCOlct (띄어쓰기 포함한 2글자만 출력)
# tset
## ip address + 172.100.200.100
'''
1. ip sddress문자열을 슬라이싱 기법을 활용, 변수에 담아 출력
2. a,b,c,d 라는 변수에 슬라이싱 법을 통해 . 을 기준으로 각각 담는다

'''
s = "ip address = 172.100.200.100"
print(s[0:10]) # 풀이 1
address = s[0:11] # 풀이 2
print(address)

# 문제 2
a,b,c,d = s[13:16],s[17:20],s[21:24],s[25:28]  #<활용적이진 않음
print(a,b,c,d)
# 172에서 1~2까지, 100에서 1에서 0까지, 200에서 2에서 0까지, 100에서 1에서 0까지
# a,b,c,d 세션에 나누어 입력하면 숫자와 띄어쓰기까지 출력됨

#문제 3
print(f"{a}{b}{c}{d}") # 오롯이 숫자만(띄어쓰기 비포함) 출력

# 입력구현 (input = 약어 ip)
#  a = imput()  << 입력을 기다리는중
# print("okay") < 코드가 띄어져 있다. 대기하고 있는중이다
# 파이썬 코드가 실행이 되서 끝이 났을경우 컴퓨더입장이에서는 입력값을 기억할 필요가 없다
# a = input()
# 파이썬에서 숫자를 입력해도 무조건 스트링타입(문자)
"""
입력을 몇가지 변수에 담아서 f-string, 문자 붙이기, 문자 반복하기 등 
여러 기술을 활용해 출력해보자
"""
# f-string 이용하여 문자 붙이기
a = "9"
b = "16"
print(f"나의 생일은 {a}월 {b}일 입니다")
# 문자반복하기
str10 = "37세"
print(str10 * 3)
# 문자이어붙이기
str12 = "생일을 "
str13 = "축하해주세요"
print(str12+str13)
str14 = str12+str13

# 형변환
# ptint(type(a)) 숫자를 문자로 입력하는 
# b = int(a) a는 문자니까 숫자로 바꿔라

#print(type(a))
#b = int(a)
#print(type(b))

#a = 1  # < 숫자를 문자로 바꿀수 있다
#print(type(str(a)))  # < 안에서 밖으로 읽는다 

#@ 문자열 고유 기능 
s = 'weniv CEO licat'
print(s.lower()) #<'너가 입력한 문자를 소문자로 바꿔준다

m = "i LOVE you" #< 원본은 훼손되면 안된다
print(m.lower())
# 새로운변수를 만들어서 할당하는게 낫다, 오리지널 원본은 절대로 회손되면 안된다

# find(터미널에 못찾을경우-1 반영), index(에러를 반영)
s = 'weniv CEO licat'
print(s.find("good")) # 터미널에 -1로 뜸 찾지못했다는 뜻
# print(s.index("good")) # ValueError: substring not found <찾지 못할경우 터미널에 에러가 뜸
print(s.find("weniv")) # 0이 나오는경우 글자의 시작점 숫자가 출력
print(s.find("licat")) # 10이 나오는경우 글자의 시작접 숫자가 출력

print(s.index("weniv")) # 문자에서 찾았을경우, 숫자로 표기되지만
print(s.index("licat"))  # 에러가 났을경우, 에러가 터짐 

# count 문구에서 특정문자를 찾는것
print(s.count("i")) 

# replace 특정문구를 찾아 변경
s2 = s.replace("CEO","CTO") 
print(s2)

# split (쪼갠다)
s3 = "weniv-corp"
# s3.split (공백을 기준으로 나눔)
# s3.split("-") ("-" 기준으로 나눔)
s4,s5 = s3.split("-")
print(s4,s5)

'''
입력이 들어온다. 키 몸무게 성별 나이 이름
예시 180 60 남 25 김아무개
이것을 공백을 기준으로 쪼개어 각 변수에 담아 출력
이름은 f-string통해 세번 반복해서 출력'''

#s10 = input()
#a,s,d,z,x = s10.split()
#print(a,s,d,z,x)

s1 = "180 60 남 25 김아무개"
print(s1,s2,s3)

str10 = "25세"
print(str10 * 3)

