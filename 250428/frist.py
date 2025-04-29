
# 정수

a = 10
b = 20
c = 0
d = -40

print(type(a),type(b),type(c),type(d))
print(int(9.3333))

# 실수
number1 = 3.12
number2 = -0.12
print(type(number1),type(number2))
print(float(3))


## 무한대
x = float("int")
y = float("-inf")

# split

a = "a-b-c" # 스플릿 : 나눈다
a = 123456-1122335 # 주민번호 앞자리, 뒷자리, 성별숫자로 구분가능
c,d = a.split("-")
print(c)
