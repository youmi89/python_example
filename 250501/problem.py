
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
#speed = float(input("시속을 입력하세요 (60km/h): "))
#time = float(input("시간을 입력하세요 (2시간, h): "))
#distance = speed * time
#print(f"총 이동 거리는 {distance} km입니다.")

# 문제 6
a = "안녕하세요."
s = "반갑습니다."
print(a + s)

# 문제 7
#inch = float(input("10:"))
#cm = inch * 2.54
#print(f"{inch}인치는 {cm}센치미터 입니다.")

# 문제 8
meal_cost = int(input("50000 (원): "))
tip_percent = int(input("15 (%): "))
tip_amount = meal_cost * (tip_percent // 100)
total_amount = meal_cost + tip_amount

print(f"\n팁 금액: {tip_amount}원")
print(f"총 지불 금액: {total_amount}원")

# 문제 9
#height_cm = float(input("170cm:"))
#weight_kg = float(input("65kg:"))
#weight_m = height_cm / 100
#bmi = weight_kg / height_m * 2
#print(f"bmi는{bmi:.2f}입니다.")

# 문제 10
#nums = input("10 20 30 40 50:")
#num_list = list(map(int,nums.split()))
#print(f"첫번째숫차: {num_list[0]}")
#print(f"마지막숫자: {num_list[-1]}")
