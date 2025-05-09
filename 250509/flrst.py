# 복습 (튜플)
# 수정, 추가, 제거 안됨

#a = (1, 10, 1, 2, 3)

# 슬라이싱
#b = a[2:5]  # 1,2,3 추출
#c = a[1]  # 10 추출

# 기능
#c = a.coubt(1)  # 2 추출
#d = a.index(1)  #

# 셋(set) 중복을 허용하지 않는 순서없는 자료형
# 중괄호사용
a = {1, 2, 3, 1}
print(a)  # 1, 2, 3
print(len(a)) # 3

# 형변환 list -> set
a = [1, 1, 1, 2, 2, 3]
b = set(a)  #중복제거, 인덱스가 안됨
print(b)
c = list(b)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"합집합: {set1 | set2}") #중복되는거 빼고 나열
print(f"교집합: {set1 & set2}") #공통적인거
print(f"차집함: {set1 - set2}") 
print(f"차집합: {set2 - set1}")
print(f"대칭 차집합: {set1.symmetric_difference(set2)}")
print(f"set1이 set2의 부분집합인가? {set1.issubset(set2)}")

# set -순서를 보장하지 않음, 중복은 없음, 실무에서 많이 사용
fruits = {'사과', '딸기', '바나나'}

fruits .add('오렌지') #<추가시 add를 사용
print(fruits)

fruits.remove('사과') # 뺄때 remove사용
print(fruits)

# 딕셔너리_ dict()
# 키(key)와 값(value)의 쌍으로 이루어진 자료형.
# 실생활의 사전과 비숫한 구조를 가지고 있어 딕셔러니라 함
my_dict = {"me": "길동"} 
my_dict2 = dict()
my_dict = {'me':[1,2,3],"me" : "good"}  
# 키만 알면 여러가지 데이터에 접근할수 있다
print(my_dict)

#딕셔너리 데이터 추가
dict4 = dict()
dict4['max'] = [1, 2, 3, 4]
print(dict4)

#딕셔너리의 키는 중복이 되지 않는다.
person = {'name': 'licat', 'age': 25, 'height': 165.5}
print(f"이름은 : {person["name"]} 입니다.")
print(f"나이는 : {person["age"]} 입니다.")

# 데이터 수정
person["age"] = 30
person["weight"] = 100
print(person)

# 데이터 삭제
del person["height"] # < del앞에 붙이고 실행
print(person)
person["age"] = None # < 키를 남기고 값을 없애고 싶을때

a = {"good" : ["a", "b", "c"]}
a["good"].remove("c")
print(a)

# 딕셔너리(.append) < 리스트 추가
b = {"good1": {"good2": [1, 2, 3, [1, 2, 3]]}}
b["good1"]["good2"][3].append(4)
print(b)

#person = {"name": "licat", "age: 25, "city": seoul}

city = person.get('city',"없는뎅")
print(city)
city2 = person.get('city2', "없는뎅")
print(city2)

person_keys = person.keys()
print(person_keys)
a = list(person_keys)
print(a)

# 전체를 추출
person_items =person.items()
print(person_items)
c =list(person_items)
print(c)
print(type(person_items))

# 반복문
s = 'hello' # 한글자씩 출력
for i in s:  
    print(i)
# < for, 반복문 왼쪽에서부터 읽는다, 
# h를 i라는 또하나의 변수에 담는다
# s라는 문자열에 i에 한글짜씩 들어가 출력
a = [1,2,3,4,5,6, "good"]
for i in a:
    print(i)

# < range 범위, 0~4999까지 순회가능한 데이터를 만든다 
# range(10,50) <10부터 50까지의 범위를 말함
#for i in range(5000):
#    print(i)

# range(1,11,2) 1부터 10까지 두단계씩 점프 <오름차순
for i in range(1,11,2):
    print(i)

# 내림차순
for i in range(10,1,-1):
    print(i)

# 문제 1 (1부터 100까지 출력)
for i in range(101):
    print(i)

# 문제 2 (2부터 50까지 짝수만 출력)
for i in range(2,51,2):
    print(i)

# 문제 3 (10부터 -1까지 출력)
for i in range(10,-2,-1):
    print(i)

for i in range(1,100): # 1에서 99까지 반복
    
    if i % 3 == 0: # 3의 배수만출력
        print(i)
for i in range(2,10): # 2부터 9까지 반복,구구단활용가능
    for j in range(1,10):
        print(f"{i} * {j} = {i*j}") # 구구단만들기
