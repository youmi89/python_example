
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

# 문제 13
#full_name = input("홍 길동")
#print(f"Initials: {first_initial}.{last_initial}")



