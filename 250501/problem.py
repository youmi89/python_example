
# 문제 1
str1 = "김개똥님"
str2 =  "안녕하세요."
print(str2 + str1)

# 문제 2
a = "안녕"
print(a*3)

# 문제 3
birth_year = input("1995년")
birth_year = int(1995)
age = 2025 - 1995
print(f"당신의 나이는{age}세 입니다.")

# 문제 4
import math
r = input("5")
r = float("5")
area = math.pi * 5 * 5
print(f"반지름이 {r}인 원의 넓이는{area:78.5} 입니다.")

# 문제 5
speed = 60
time = 2
distance = speed * time
print(f"총 이동 거리는 {distance} km입니다.")

# 문제 6
a = "안녕하세요."
s = "반갑습니다."
print(a + s)

# 문제 7
inch = 10
cm = inch * 2.54
print(f"{inch}인치는 {cm}센치미터 입니다.")

# 문제 8
# 사용자 입력 받기
meal_cost = int(50000)
tip_percent = int(15)
tip_amount = meal_cost * tip_percent // 100
total_amount = meal_cost + tip_amount
print(f"\n팁 금액: {tip_amount}원")
print(f"총 지불 금액: {total_amount}원")

# 문제 9
height_cm = float(170)
weight_kg = float(65)
weight_m = height_cm / 100
bmi = weight_kg / (weight_m ** 2)
print(f"\n bmi는 {bmi:.2f}입니다.")

# 문제 10
numbers = "20 40 60 80 100".split()
print(f"첫번째숫자: {numbers[0]}")
print(f"마지막숫자: {numbers[-1]}")

# 문제 11
a = 10
b = 20
a, b = b, a
print(f"\n교환 후 a ={a}, b = {b}")

# 문제 12
string = ("파이썬 프로그래밍")
print(len(string))
print(f"첫번째 글자:", string[0])
print(f"마지막 글자:", string[-1])

# 문제 13 (이니셜 만들기)
#full_name = input("홍 길동")
#print(f"Initials: {first_initial}.{last_initial}")

# 문제 14
number = 3.14159
print(f"{number:.2f}")

# 문제 15
age = int(input("나이를 입력하세요:"))
if age < 19:
    print("미성년자")
elif age <= 34:
    print("청년")
elif age <= 64:
    print("중장년")
else:
    print("노년")

# 문제 16
#text = int(input("문자를 입력하세요:"))
#    if char =='':
#        space_count += 1
#    elif'0' <= char <= '9':
#        digit_count += 1
#    elif('a' <= char <= 'z') or ('A' <= char <= 'Z'):
#        alpha_count += 1
#    else:
#        special_count += 1
#print("공백 수:", space_count)
#print("숫자 수:", digit_count)
#print("문자 수:", alpha_count)
#print("특수문자 수:", special_count)

# 문제 17
values = [0,1,"","hello","0","False"]

for v in values:
    print(f"{repr(v)} -> {bool(v)}")

# 문제 18
num =  int(input("숫자를 입력하세요: "))

if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

# 문제 19
str = ("사과 바나나 딸기 오렌지")
splitted_str =  str.split()
print(splitted_str)

# 문제 20
#temp = input()
#temp = float(temp)
#unit = input() # C 또는 F
#if unit == "C": # 섭씨라면
#    convert = temp * 9/5 + 32
#    print(f"{temp}.C는 {convert}.F입니다.")
#elif unit == "F": # 화씨라면
#    convert = (temp-32) * 5/9
#    print(f"{temp}.F는 {convert}.C입니다.")
#else: #c와 f가 아닌 다른 값이 입력 됐을 때
#    print("잘못입력하였습니다.")

### ex
food = input()

if food.find("짜장") != -1:
    if "쟁반" in food:
        print("쟁반짜장입니다")
else:
    print("짬뽕입니다")

# 문제 21
s = ("Python Programming")

print(s.lower()) # 문자전체 소문자 출력
print(s.upper()) # 문자전체 대문자 출력
print(s.title()) # 앞글자 대문자로 출력

# 문제 22
s = ("파이썬프로그래밍")
print(string[0:3]) # 앞에 3자리 출력
print(string[-3:]) # 끝에 3자리 출력
print(string[::-1]) # 거꾸로 출력

# 문제 23
s = ("파이썬은 간결하고 배우기 쉬운 프로그래밍 언어입니다.")
print(s.find("프로그래밍"))

# 문제 24

a = ("Hello World")
print(a.replace("o", "*")) # replace>>찾고자 하는 문자를 다른문자로 변경해주는 코드

# 문제 25
s = ("banana")
print(s.count('a')) # 문자열에서 "a"는 몇번 포함 되어있는지 출력하기위한 코드

# 문제 26




# 문제 27

ex = "python"
print(ex.ljust(10, "*")) 

# 문제 28



# 문제 29
#text = "Hello, World! How are you?"



