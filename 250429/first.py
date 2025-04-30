
x,y =  10, 100

print(x==y)

x,y = 10, 10
print(x>y) # 초과
print(x>=y) # 이상

print(x<y) # 미만
print(x<=y) # 이하

print('apple' < 'banana') # 결과  : true
a ='1234567890'
print(len(a)) # lin(변수) 는 변수의 문자 수를 가져온다.

"""
input() 두 번을 사용하려, 두개의 변수의 임의의 문자열을 넣고,
len() 을 사용하려 문자의 수를 변수에 넣는다

print('첫번째 변수의 문자 수는 {문자의 수}이다.')
print('두번째 변수의 문자 수는 {문자의 수}이다.')
"""

s1 = input() # s1이라는 변수에 문자열을 입력
s2 = input() # s2이라는 변수에 문자열을 입력

s3 = len(s1) # len() 을통해 s1 변수의 문자열 수를 가져온다.
s4 = len(s2) # len() 을통해 s2 변수의 문자열 수를 가져온다.

print(f"첫번째 변수의 문자 수는 {s3} 입니다.")
print(f"첫번째 변수의 문자 수는 {s4} 입니다.")


money = 500000000000000000000000000000000000

print(f"{money:,} 원 갖고싶어요")


# and  연산

## 다른 언어에서는 

a = True
b = True
c = a and b
d = 10 > 5 and 10 < 5 # d = true and false
print(d)

f = 10 >= 10 or False # 앞에 이미 True 나왔기 때문에 뒤에 값이 같다


st = "modulabs is good"

sta = "good" not in st # "good"이라는 문자가 st에 없니?
sta2 ="good" in st # "good"이라는 문자가 st에 있니?

#if조건 (~하면 ~해라) 

# ~ elif (2로 나눴을때 조건문이냐) 

# ~ else 나머지 (이도저도아닐때사용)

if a > 10:
    print("good")
elif b == 20:
    print("20입니다.")
elif a == 10:
    print("10입니다.")
else:
    print("이도저도 아니다.")


age = 19
if age <= 19:
    print("청소년입니다.")
elif age < 30:
    print("성인입니다.")
else:
    print("30세 이상입니다.")

yyyy,mm,dd = input().split()
yyyy,mm,dd = int(yyyy),int(mm),int(dd)
if yyyy % 2 == 0:
    print("짝수 년도에 태어났습니다.")
else:
    print("홀수 년도에 태어났습니다.")

# 파이썬은 들여쓰기가 중요하다


