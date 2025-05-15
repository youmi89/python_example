
#1
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])

#2
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.remove(2)
print(numbers)

#3
total = 0
for i in range(1, 5):
    total += i
print(total)

#4
score = 75
if score >= 90:
    result = "A"
elif score >= 80:
    result = "B"
elif score >= 70:
    result = "C"
else:
    result = "D"
print(result)

#5
text = "Python Programming"
print(text[7:13])

#6
student = {"name": "Kim", "age": 20, "grade": "A"}
student["age"] = 21
print(student["age"])

#7
result = 0
for i in range(3):
    for j in range(2):
        result += i + j
print(result)

#8
a = 5
b = 10
c = 15
if a > b:
    print("A")
elif b > c:
    print("B")
elif a + b == c:
    print("C")
else:
    print("D")

#9
numbers = [2, 4, 6, 8, 10]
result = []
for num in numbers:
    if num > 5:
        result.append(num // 2)
print(result)

#10
data = {"a": [1, 2, 3], "b": [4, 5, 6]}
result = 0
for key in data:
    for num in data[key]:
        if num % 2 == 0:
            result += num
print(result)

#11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        print(even_numbers)

#12
scores = {"국어": 85, "영어": 90, "수학": 78, "과학": 92}
total = sum(scores.values())
average = total / len(scores)
print("평균 점수", average)

#13
s = ("Python Programming")
result = s.replace(" ","").lower()
print(result)

#14
end = int(input("숫자를 입력하세요:"))
total = 0
for i in range(1, end + 1):
    if i % 3 != 0:
        total += i
print("3의 배수를 제외한 합:", total)

#15
temperature = float(input("온도를 입력하세요:"))
if temperature < 0:
    print("얼음")
elif temperature < 100:
    print("물")
else:
    print("수증기")

