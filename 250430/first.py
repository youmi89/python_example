

# 문제 1) 키와 몸무게를 입력
a = 160
b = 55
print(f"키는 {160}cm 이고, 몸무게는 {55}kg 입니다.")
# 풀이
# a,b = input().split()
# a,b = int(a),int(b)

# 문제 2)
# 키(a)가 130 이상이면 a, 150이상이면 b, 170이상이면 c, 180이상이면 d를 출력
a = 185
if a >= 180:
    print("a")
elif a >= 170:
    print("b")
elif a >= 150:
    print("c")
else:
    print("d")

# a,b = input().split()
# a,b = int(a),int(b)

# 문제1)
# 시험 점수를 입력받아 90 ~ 100점은 A, 
# 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 
# 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

score = int(input("시험점수"))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("c")
elif score >= 60:
    print("D")
else:
    print("F")

# 다른버전(바로 등급출력되는 풀이)
score = 20
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("c")
elif score >= 60:
    print("D")
else:
    print("F")
# 실행하기 전에 맨 위에 스코어 숫자만 바꾸면 된다


# and or 연산활용
# and는 모두가 참이여야 한다 
# a = 10
# b = 20
# if a == 10 and b == 20:
#    print("good")
# else:
#    print("no")

# 문제 1)
'''a,b,c 를 입력 받는다.
a가 100이고 b가 200이상이면 "a"를 출력
b가 1이면 "b"
이도저도 아니면 "c" 출력
'''
#풀이
a,b,c = int(input()), int(input()), int(input()),

if a == 100 and b >= 200:
    print(a)
elif b == 1:
    print(b)
else:
    print(c)

# 문제 1)
"""
 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
 예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다. 
 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다. 
 3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.

3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.
"""

a,b,c = input("3개의 주사위 눈을 띄어쓰기로 구분하여 입력하세요: ").split()
a,b,c = int(a),int(b),int(c)
# 같은 눈이 3개일 경우
if a == b == c:
    price = 10000 * a *1000
# 같은 눈이 2개일 경우
elif a == b:
    price = 1000 + a * 100
elif a == c:
    price = 1000 + a * 100
elif b == c:
    price = 1000 + b * 100
else:
    price = 0
# 모두 다른 눈일 때 최대값 찾기
if a != b and b != c and a != c:
    temp = a
    if b > temp:
        temp = b
    if c > temp:
        temp = c
    price = temp * 100

print(f"상금: {price}원")



